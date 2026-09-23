#!/usr/bin/env python3
"""Audit DOCX image placement, effective resolution, and optional PDF readability."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET

from PIL import Image

NS = {
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
}
EMU_PER_INCH = 914400.0


def q(ns: str, tag: str) -> str:
    return f"{{{NS[ns]}}}{tag}"


def resolve_target(target: str) -> str:
    return str(PurePosixPath("word") / PurePosixPath(target))


def inspect_docx(path: Path, min_ppi: float, target_ppi: float) -> dict:
    result = {
        "docx": str(path),
        "inline_images": 0,
        "anchored_images": 0,
        "images": [],
        "errors": [],
        "warnings": [],
    }
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
        rel_root = ET.fromstring(zf.read("word/_rels/document.xml.rels"))
        rels = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in rel_root.findall("pr:Relationship", NS)
        }
        result["anchored_images"] = len(root.findall(".//wp:anchor", NS))
        if result["anchored_images"]:
            result["errors"].append("Floating or anchored images are present")

        for idx, inline in enumerate(root.findall(".//wp:inline", NS), start=1):
            result["inline_images"] += 1
            extent = inline.find("wp:extent", NS)
            blip = inline.find(".//a:blip", NS)
            item = {"index": idx}
            if extent is None or blip is None:
                item.update(status="FAIL", error="Missing extent or image relationship")
                result["errors"].append(f"Image {idx}: {item['error']}")
                result["images"].append(item)
                continue
            rid = blip.attrib.get(q("r", "embed"))
            target = rels.get(rid or "")
            if not target:
                item.update(status="FAIL", error="Broken image relationship")
                result["errors"].append(f"Image {idx}: {item['error']}")
                result["images"].append(item)
                continue
            member = resolve_target(target)
            try:
                with zf.open(member) as fh:
                    image = Image.open(fh)
                    px_w, px_h = image.size
            except Exception as exc:
                item.update(status="FAIL", error=f"Cannot read {member}: {exc}")
                result["errors"].append(f"Image {idx}: {item['error']}")
                result["images"].append(item)
                continue

            in_w = int(extent.attrib["cx"]) / EMU_PER_INCH
            in_h = int(extent.attrib["cy"]) / EMU_PER_INCH
            ppi_x = px_w / in_w if in_w else 0.0
            ppi_y = px_h / in_h if in_h else 0.0
            src_ratio = px_w / px_h
            display_ratio = in_w / in_h if in_h else 0.0
            distortion = abs(display_ratio / src_ratio - 1.0) * 100 if src_ratio else math.inf
            effective_ppi = min(ppi_x, ppi_y)
            status = "PASS"
            if effective_ppi < min_ppi or distortion > 2.0:
                status = "FAIL"
                result["errors"].append(
                    f"Image {idx}: effective ppi={effective_ppi:.1f}, distortion={distortion:.2f}%"
                )
            elif effective_ppi < target_ppi:
                status = "WARN"
                result["warnings"].append(
                    f"Image {idx}: effective ppi={effective_ppi:.1f} below target {target_ppi:.0f}"
                )
            item.update(
                {
                    "relationship_id": rid,
                    "member": member,
                    "pixels": [px_w, px_h],
                    "display_inches": [round(in_w, 3), round(in_h, 3)],
                    "effective_ppi": round(effective_ppi, 1),
                    "aspect_ratio_deviation_percent": round(distortion, 3),
                    "status": status,
                }
            )
            result["images"].append(item)
    return result


def inspect_pdf(path: Path) -> dict:
    info = {"path": str(path), "readable": False}
    proc = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, check=False)
    info["pdfinfo_exit"] = proc.returncode
    if proc.returncode == 0:
        info["readable"] = True
        for line in proc.stdout.splitlines():
            if line.startswith("Pages:"):
                info["pages"] = int(line.split(":", 1)[1].strip())
                break
    else:
        info["error"] = proc.stderr.strip() or "pdfinfo failed"
    return info


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docx", required=True, type=Path)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--json", dest="json_path", type=Path)
    parser.add_argument("--min-ppi", type=float, default=150.0)
    parser.add_argument("--target-ppi", type=float, default=220.0)
    args = parser.parse_args()

    report = inspect_docx(args.docx, args.min_ppi, args.target_ppi)
    if args.pdf:
        report["pdf"] = inspect_pdf(args.pdf)
        if not report["pdf"]["readable"]:
            report["errors"].append("Final PDF is not readable by pdfinfo")
    report["overall"] = "FAIL" if report["errors"] else (
        "WARN" if report["warnings"] else "PASS"
    )
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    print(payload)
    if args.json_path:
        args.json_path.parent.mkdir(parents=True, exist_ok=True)
        args.json_path.write_text(payload + "\n", encoding="utf-8")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
