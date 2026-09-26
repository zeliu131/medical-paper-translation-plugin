# Deliverable Contract

## Paths and five official files

Default source root: `D:\EEC_metabolism\literature\文献合集` (main article and any verified supplementary PDFs). Default destination: `D:\EEC_metabolism\literature\翻译`. Respect an explicit user-specified path for a task. Do not alter source files or existing output directories.

For each article, use `<destination>\<full original English article title>\vN\` as the edition directory. Collapse accidental whitespace and replace only Windows-forbidden path characters; never substitute an author-year or `_supplement_bilingual` directory name. Put verified supplements after the main article/references inside the same edition. Choose the next unused `vN` and do not overwrite any earlier edition. If a required supplement is absent, record that fact in the QC report and deliver the main-paper edition without fictitious supplementary content.

Inside the edition directory, deliver exactly five user-facing files, named with the same sanitized original English article title:

1. `1阅读_<English article title>.docx`
2. `1阅读_<English article title>.pdf`
3. `2学习_<English article title>.docx`
4. `2学习_<English article title>.pdf`
5. `3词表_<English article title>.xlsx`

The reading edition retains paragraph-aligned English/Chinese text, figures, bilingual captions/tables and, when present, the translated supplement. The learning edition contains all the same content plus paragraph-specific learning blocks drawn from the checked glossary. The Excel glossary contains complete source-aware article and supplement terms with the two new morphology columns. Preserve all existing styles, markup, and figure-quality requirements unless the user specifies a change.

Keep manifests, SHA256, paragraph mapping, translation/QC notes, pronunciation and etymology sources, script logs, rendered-page audit images, and any optional critical-reading notes in `work_records\` inside the edition directory. These are necessary working evidence, not extra official reading files. Keep a single cross-paper index under `<destination>\_shared\` and count it separately from the five files per paper. If Windows length limits obstruct a full filename, preserve the full article-title folder and log the minimal shortening of the file stems; do not silently truncate titles.

## QC report minimums

- All source PDFs, verified article/supplement linkage, pages, bytes, and SHA256
- Extracted article and supplementary section/paragraph/caption/table-note counts
- English/Chinese pair counts and unmatched IDs in **both** editions
- Figure/table expected and delivered counts per source PDF, including supplements
- Image pixel dimensions, displayed dimensions, effective ppi, and aspect-ratio deviation in **both** editions
- Inline versus anchored image count for each DOCX
- Each DOCX and corresponding PDF rendered page counts and every-page visual inspection status
- Glossary header/order, one-word-at-a-time IPA checks, new-line wrapping in morphology cells, and learning-block-to-glossary IDs
- Shared-index update status, citations, conflicts, and unchanged/manual learner states
- Corrected defects and remaining source-limited exceptions

## Final response

List the five deliverable paths and version. State whether supplements were included and how they were verified. Report missing supplements or source-limited exceptions briefly. Do not claim completion unless both DOCX/PDF pairs pass structural and every-page visual review and the glossary is checked.
