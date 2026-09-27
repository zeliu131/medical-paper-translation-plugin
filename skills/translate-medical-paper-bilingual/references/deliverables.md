# Deliverable Contract

## Paths and three official files

Default source root: `D:\EEC_metabolism\literature\文献合集` (main article and any verified supplementary PDFs). Default destination: `D:\EEC_metabolism\literature\翻译`. Respect an explicit user-specified path for a task. Do not alter source files or existing output directories.

For each article, use `<destination>\<full original English article title>\vN\` as the edition directory. Collapse accidental whitespace and replace only Windows-forbidden path characters; never substitute an author-year or `_supplement_bilingual` directory name. Put verified supplements after the main article/references inside the same edition. Choose the next unused `vN` and do not overwrite any earlier edition. If a required supplement is absent, record that fact in the QC report and deliver the main-paper edition without fictitious supplementary content.

Inside the edition directory, deliver **exactly three user-facing files**, named with the same sanitized original English article title:

1. `1阅读_<English article title>.docx`
2. `1阅读_<English article title>.pdf`
3. `3词表_<English article title>.xlsx`

The **single** reading edition retains paragraph-aligned English/Chinese text, pale-yellow **and underlined** terminology in both languages, complete original figures, bilingual captions/tables and, when present, the translated supplement. The Excel glossary contains beginner-level source-aware terms, verified IPA, and the two morphology columns. **Do not create `2学习_` DOCX/PDF or paragraph-specific learning blocks.** Keep prior editions intact.

Keep manifests, SHA256, paragraph and term-to-paragraph markup mappings, translation/QC notes, pronunciation and etymology sources, script logs, rendered-page audit images, original-versus-extracted-versus-final comparisons for **every** figure, and any optional critical-reading notes in `work_records\` inside the edition directory. These are working evidence, not extra official reading files. Keep one cross-paper index under `<destination>\_shared\` and count it separately from the three files per paper. If Windows length limits obstruct a full filename, preserve the full article-title folder and log minimal shortening of file stems.

## QC report minimums

- All source PDFs, verified article/supplement linkage, pages, bytes, and SHA256
- Extracted article and supplementary section/paragraph/caption/table-note counts
- English/Chinese pair counts and unmatched IDs in the reading edition.
- Glossary term/sense count and beginner-level selection rationale; **every** paragraph/caption inspected, including zero-highlight paragraphs; selected occurrences, English and Chinese highlighted+underlined counts, and zero unmatched pairs/glossary IDs.
- Figure/table expected and delivered counts per source PDF, including supplements. For **every** figure, retain original, extracted, and final comparison images; record panel/label inventory, left/right/top/bottom pass/fail, source pixels, displayed size, effective ppi, and aspect-ratio deviation. Fig. 1 must preserve the outermost left labels and bottom panels/labels.
- Inline versus anchored image count for the reading DOCX; rendered DOCX/PDF page counts and every-page visual inspection status. Verify yellow highlighting and underlining remain visible in the final PDF.
- Glossary header/order, one-word-at-a-time IPA checks, and new-line wrapping in morphology cells.
- Shared-index update status, citations, conflicts, and unchanged/manual learner states
- Corrected defects and remaining source-limited exceptions

## Final response

List the three deliverable paths and version. State whether supplements were included and how they were verified. Briefly report glossary count, paired-highlight audit, original-to-final figure audit (especially Fig. 1), and any missing supplement or source limitation. Do not claim completion unless the reading DOCX/PDF passes structural and every-page visual review, **all** figures are complete, and the glossary and markup are checked.
