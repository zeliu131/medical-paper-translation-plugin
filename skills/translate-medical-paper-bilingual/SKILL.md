---
name: translate-medical-paper-bilingual
description: Translate biomedical or clinical research PDFs into paragraph-aligned English-Chinese study editions, preserving complete text, tables, high-resolution original figures, bilingual captions, terminology highlighting, and references. Use when the user asks Codex to translate, closely read, or create a bilingual Chinese-English DOCX/PDF from a medical paper, especially when figure clarity, paragraph correspondence, professional terminology, and page-layout verification matter.
---

# Translate Medical Paper Bilingual

Produce a faithful study edition, not a summary. Keep author text, translator notes, and critical appraisal visibly separate.

## Load required guidance

1. Read `references/translation-standard.md` before translating.
2. Read `references/figures-layout-qc.md` before extracting figures or building the document.
3. Read `references/deliverables.md` before naming outputs or reporting completion.
4. Use the available PDF, documents, and spreadsheet skills for source inspection, DOCX/PDF generation, glossary work, rendering, and visual QA. Their artifact and render requirements remain mandatory.

## Workflow

### 1. Inventory and preserve sources

- Resolve the exact input PDF and any supplements. Record filename, real format, pages, bytes, and SHA256.
- Never overwrite, rename, move, or delete source files.
- Inspect supplements independently. Missing supplements do not block the main paper unless the user explicitly requires a complete supplement edition.
- Create a versioned output directory beside the source or at the user-specified location.

### 2. Reconstruct the article correctly

- Extract text with a layout-aware route and verify reading order against rendered source pages.
- Remove repeated preprint layers, running headers, footers, and page numbers only after visual confirmation.
- Preserve title, authors, affiliations, summaries, abstract, keywords, headings, body, methods, results, discussion, conclusions, declarations, captions, tables, citations, and references.
- Build a section/paragraph manifest before translation. Give every source paragraph a stable ID and pair it with exactly one Chinese translation block.
- Preserve citations, values, units, gene symbols, drug names, concentrations, durations, sample sizes, and statistical notation exactly.

### 3. Translate paragraph by paragraph

- Place each English paragraph immediately before its Chinese translation.
- Translate for a clinical/pathology reader: accurate, fluent, and professionally conventional.
- Preserve evidential strength. Never upgrade `may`, `suggest`, `potential`, `associate`, or `hypothesize` to proof or causality.
- Distinguish genes, transcripts, proteins, receptors, drugs, metabolites, assays, biological replicates, and technical replicates.
- Keep references in the source language unless the user asks otherwise.
- Add interpretation only in a separately labeled reading-notes document, never inside the faithful translation.

### 4. Add synchronized learning markup

- Select useful medical, pathological, pharmacological, molecular, and methods vocabulary; avoid highlighting ordinary words excessively.
- Apply the same underline and pale-yellow highlight to the complete English term and its exact Chinese counterpart.
- Highlight primarily on first occurrence in each major section.
- Produce a glossary with source section, English term, part of speech, verified textbook-style broad IPA, professional Chinese, plain-language Chinese explanation, source sentence, collocation, and translation note. Use the familiar Chinese English-classroom 48-sound notation described in `references/translation-standard.md`; write long vowels with `:` (for example, `/ˈti:tʃə/`), and retain stress marks. For a phrase, transcribe **each word separately** in source order and join complete `/.../` transcriptions with ` | `; never collapse the phrase into one IPA string. Prefer verified British learner-dictionary pronunciations when available. Do not leave a pronunciation cell blank, use `NOT_VERIFIED`, or invent a pronunciation to fit the textbook chart.

### 5. Preserve figures and tables

- Follow `references/figures-layout-qc.md` exactly.
- Extract the original figure at native quality when possible; otherwise crop a 300-400 dpi rendering of the source page.
- Include every panel label, axis, legend, scale bar, significance mark, and inset. Do not include surrounding body text in the crop.
- Insert figures as inline objects, never floating/anchored objects.
- Preserve aspect ratio. Put the English caption and then the Chinese caption immediately below the same figure.
- Keep figure, English caption, and Chinese caption together. Insert a page break before the figure if the block cannot fit cleanly.
- Rebuild tables when needed for legibility; retain an original-table image when it helps audit fidelity. Never change printed values silently.

### 6. Build DOCX and PDF

- Default to a polished A4 portrait study edition unless the user specifies another format.
- Use readable English and Chinese fonts, a restrained hierarchy, searchable text, page numbers, and a clear unofficial-translation notice.
- Avoid floating text boxes and floating pictures.
- Generate DOCX first when it is the stable layout source, then export the same document to PDF. Do not maintain two independently authored versions.
- Use versioned filenames and never overwrite prior editions.

### 7. Run hard QA gates

- Verify source-section completeness and one-to-one English/Chinese paragraph pairing.
- Verify expected figure and table counts against the article.
- Run `scripts/audit_bilingual_docx.py --docx <docx> --pdf <pdf> --json <report.json>`.
- Treat anchored images, broken image relationships, aspect-ratio distortion over 2%, unreadable figures, clipped captions, missing panels, or missing paired paragraphs as release blockers.
- Target at least 220 effective ppi at displayed size. Allow 150-219 ppi only when the source itself is limiting and every label remains legible at 100% zoom; document the exception. Below 150 ppi is a blocker.
- Render the DOCX and final PDF to page PNGs. Inspect every page at 100% zoom, not a sample.
- Check for overlap, clipping, font substitution, tofu boxes, table overflow, orphan captions, excessive blank space, misplaced figures, and inconsistent page breaks.
- Fix, rebuild, and re-render until all pages pass.

## Completion rule

Do not claim completion from file existence or structural checks alone. Completion requires content reconciliation, machine audit, and visual inspection of every final page. If a supplement is missing, deliver a clearly named main-paper edition and record the supplement as pending rather than stopping the main translation.
