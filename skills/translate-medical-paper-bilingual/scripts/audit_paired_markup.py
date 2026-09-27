#!/usr/bin/env python3
"""Check bilingual paragraph order and explicit paired yellow-underlined DOCX terms.

Manifest shape: {"paragraphs": [{"id": "S01-P001", "english": "...",
"chinese": "...", "terms": [{"id": "...", "glossary_id": "...",
"english": "...", "chinese": "..."}]}]}.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\u00a0", " ")).strip()


def paragraph_info(element: ET.Element) -> dict:
    text = []
    styled_streaks = []
    current = ""
    for run in element.iter(W + "r"):
        run_text = "".join(node.text or "" for node in run.iter(W + "t"))
        if not run_text:
            continue
        text.append(run_text)
        props = run.find(W + "rPr")
        highlight = props.find(W + "highlight") if props is not None else None
        underline = props.find(W + "u") if props is not None else None
        yellow = highlight is not None and highlight.get(W + "val") == "yellow"
        underlined = underline is not None and underline.get(W + "val", "single") not in ("none", "false", "0")
        if yellow and underlined:
            current += run_text
        elif current:
            styled_streaks.append(compact(current))
            current = ""
    if current:
        styled_streaks.append(compact(current))
    return {"text": compact("".join(text)), "marked_spans": styled_streaks}


def inspect(docx: Path, manifest: Path) -> dict:
    records = json.loads(manifest.read_text(encoding="utf-8"))
    entries = records.get("paragraphs") if isinstance(records, dict) else None
    if not isinstance(entries, list) or not entries:
        raise ValueError("Manifest must have a nonempty 'paragraphs' array")
    with zipfile.ZipFile(docx) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
    body = root.find(W + "body")
    if body is None:
        raise ValueError("DOCX has no document body")
    paragraphs = [paragraph_info(p) for p in body.iter(W + "p")]
    paragraphs = [p for p in paragraphs if p["text"]]

    report = {"docx": str(docx), "manifest": str(manifest),
              "paragraph_pairs_expected": len(entries), "paragraph_pairs_found": 0,
              "selected_occurrences": 0, "english_marked": 0,
              "chinese_marked": 0, "zero_term_paragraphs": 0, "errors": []}
    cursor = 0
    seen_ids = set()
    for record in entries:
        pid = str(record.get("id", ""))
        english = compact(str(record.get("english", "")))
        chinese = compact(str(record.get("chinese", "")))
        terms = record.get("terms")
        if not pid or pid in seen_ids or not english or not chinese or not isinstance(terms, list):
            report["errors"].append(f"Invalid, duplicate, or incomplete paragraph record: {pid!r}")
            continue
        seen_ids.add(pid)
        matching = next((i for i in range(cursor, len(paragraphs) - 1)
                         if paragraphs[i]["text"] == english and paragraphs[i + 1]["text"] == chinese), None)
        if matching is None:
            report["errors"].append(f"{pid}: English/Chinese paragraphs missing or not adjacent in source order")
            continue
        report["paragraph_pairs_found"] += 1
        cursor = matching + 2
        if not terms:
            report["zero_term_paragraphs"] += 1
        for term in terms:
            report["selected_occurrences"] += 1
            tid = str(term.get("id", ""))
            gid = str(term.get("glossary_id", ""))
            en = compact(str(term.get("english", "")))
            zh = compact(str(term.get("chinese", "")))
            if not tid or not gid or not en or not zh:
                report["errors"].append(f"{pid}: incomplete term/glossary mapping: {tid!r}")
                continue
            for label, surface, para in (("English", en, paragraphs[matching]),
                                         ("Chinese", zh, paragraphs[matching + 1])):
                if surface.casefold() not in para["text"].casefold():
                    report["errors"].append(f"{pid}/{tid}: {label} term absent from paragraph: {surface}")
                elif not any(surface.casefold() in span.casefold() for span in para["marked_spans"]):
                    report["errors"].append(f"{pid}/{tid}: {label} lacks complete yellow highlight AND underline: {surface}")
                else:
                    key = "english_marked" if label == "English" else "chinese_marked"
                    report[key] += 1
    report["overall"] = "FAIL" if report["errors"] else "PASS"
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docx", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--json", dest="json_path", type=Path)
    args = parser.parse_args()
    try:
        report = inspect(args.docx, args.manifest)
    except (ValueError, OSError, KeyError, zipfile.BadZipFile) as exc:
        report = {"overall": "FAIL", "errors": [str(exc)]}
    output = json.dumps(report, ensure_ascii=False, indent=2)
    print(output)
    if args.json_path:
        args.json_path.parent.mkdir(parents=True, exist_ok=True)
        args.json_path.write_text(output + "\n", encoding="utf-8")
    return 1 if report["overall"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
