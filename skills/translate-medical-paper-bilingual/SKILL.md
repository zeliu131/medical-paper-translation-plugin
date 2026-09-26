---
name: translate-medical-paper-bilingual
description: Translate biomedical research PDFs and verified supplements into paragraph-aligned English-Chinese reading and vocabulary-learning DOCX/PDF editions with a medical glossary, clear original figures, and cross-paper vocabulary review. Use for medical paper translation, close reading, bilingual PDFs, or a reusable English-learning edition.
---

# Translate Medical Paper Bilingual

Produce a faithful study edition, not a summary. Keep author text, translator notes, and critical appraisal visibly separate.

## Load required guidance

1. Read `references/translation-standard.md` before translating.
2. Read `references/figures-layout-qc.md` before extracting figures or building the document.
3. Read `references/deliverables.md` before naming outputs or reporting completion.
4. Read `references/learning-and-index.md` before building the glossary or learning edition.
5. Use the available PDF, documents, and spreadsheet skills for source inspection, DOCX/PDF generation, glossary work, rendering, and visual QA. Their artifact and render requirements remain mandatory.

## Workflow

### 1. Inventory and preserve sources

- Default input root: `D:\EEC_metabolism\literature\文献合集`; default output root: `D:\EEC_metabolism\literature\翻译`. An explicit task-specific path takes precedence.
- Resolve the exact article PDF and any supplements. Verify each supplement belongs to the article using title, DOI, article metadata, or internal references; a similar filename alone is insufficient. Record filename, real format, pages, bytes, and SHA256.
- Never overwrite, rename, move, or delete source files.
- Inspect supplements independently. Missing supplements do not block the main paper unless the user explicitly requires a complete supplement edition.
- Place new output under `<output root>\<exact English article title>\vN\`; replace only Windows-forbidden filename characters, collapse redundant spaces, and preserve the title otherwise. Keep prior editions and existing legacy folders intact. Keep all verified supplements of the same paper inside the same edition, after the main article and references.

### 2. Reconstruct the article correctly

- Extract text with a layout-aware route and verify reading order against rendered source pages.
- Remove repeated preprint layers, running headers, footers, and page numbers only after visual confirmation.
- Preserve title, authors, affiliations, summaries, abstract, keywords, headings, body, methods, results, discussion, conclusions, declarations, captions, tables, citations, and references.
- Build a section/paragraph manifest for the article and each verified supplement before translation. Give every source paragraph, caption, table note, and supplementary block a stable ID and pair it with exactly one Chinese translation block.
- Preserve citations, values, units, gene symbols, drug names, concentrations, durations, sample sizes, and statistical notation exactly.

### 3. Translate paragraph by paragraph

- Place each English paragraph immediately before its Chinese translation.
- Translate for a clinical/pathology reader: accurate, fluent, and professionally conventional.
- Preserve evidential strength. Never upgrade `may`, `suggest`, `potential`, `associate`, or `hypothesize` to proof or causality.
- Distinguish genes, transcripts, proteins, receptors, drugs, metabolites, assays, biological replicates, and technical replicates.
- Keep references in the source language unless the user asks otherwise. Append verified supplements after the main article's references, with source order and page/figure/table identifiers preserved. Translate supplementary prose, legends, notes, and textual tables, and retain original graphics at source-limited maximum clarity.
- Add interpretation only in a separately labeled reading-notes document, never inside the faithful translation.

### 4. Add synchronized learning markup

- Select useful medical, pathological, pharmacological, molecular, and methods vocabulary; avoid highlighting ordinary words excessively.
- Apply the same underline and pale-yellow highlight to the complete English term and its exact Chinese counterpart.
- Highlight primarily on first occurrence in each major section.
- Produce the glossary from the article and supplements with the V2 columns and ordering plus `词根词缀释义` and `词根词缀举例` immediately after `专业中文`. Keep the intact English term and its one pronunciation cell; for a phrase, transcribe each word separately in that one cell, separated by `、`. Follow the textbook IPA and verified morphology rules in `references/translation-standard.md` and `references/learning-and-index.md`.
- Build and verify the complete glossary before the learning edition. Reuse the same paragraph records, translations, glossary entries, evidence, and figure assets for both editions. Do not ask a model to research or generate an already verified entry again; investigate conflicts, missing evidence, or a genuinely new sense when needed. Do not trade completeness or QA for fewer calls.

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
- Generate the reading DOCX and learning DOCX from the same content records, inserting paragraph-specific learning blocks only into the learning DOCX. Export each DOCX to its corresponding PDF. Do not maintain independently authored DOCX/PDF text.
- Use the next unused `vN` edition directory and the five fixed filenames in `references/deliverables.md`; never overwrite prior editions.

### 7. Run hard QA gates

- Verify source-section completeness and one-to-one English/Chinese paragraph pairing separately in both editions, including supplements.
- Verify expected figures, tables, captions, and notes against every source PDF. Confirm the five deliverables exist and each learning item is supported by a glossary entry and source ID.
- Run `scripts/audit_bilingual_docx.py --docx <docx> --pdf <pdf> --json <report.json>` on each DOCX/PDF pair.
- Treat anchored images, broken image relationships, aspect-ratio distortion over 2%, unreadable figures, clipped captions, missing panels, or missing paired paragraphs as release blockers.
- Target at least 220 effective ppi at displayed size. Allow 150-219 ppi only when the source itself is limiting and every label remains legible at 100% zoom; document the exception. Below 150 ppi is a blocker.
- Render the DOCX and final PDF to page PNGs. Inspect every page at 100% zoom, not a sample.
- Check for overlap, clipping, font substitution, tofu boxes, table overflow, orphan captions, excessive blank space, misplaced figures, and inconsistent page breaks.
- Fix, rebuild, and re-render until all pages pass.

## Completion rule

Do not claim completion from file existence or structural checks alone. Completion requires content reconciliation, machine audit, and visual inspection of every final page. If a supplement is missing, deliver a clearly named main-paper edition and record the supplement as pending rather than stopping the main translation.
