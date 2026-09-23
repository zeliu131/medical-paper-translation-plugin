# Deliverable Contract

## Default outputs

1. `<paper>_bilingual_annotated_v1.docx`
2. `<paper>_bilingual_annotated_v1.pdf`
3. `<paper>_medical_english_glossary_v1.xlsx`
4. `<paper>_critical_reading_notes_CN_v1.md`
5. `<paper>_translation_QC_v1.md`
6. `<paper>_manifest_sha256_v1.tsv`

Use `_supplement_pending` in filenames when a required supplement is absent. Create a new version when it arrives; never overwrite the prior edition.

## QC report minimums

- Source files, pages, bytes, and SHA256
- Extracted section and paragraph counts
- English/Chinese pair counts and unmatched IDs
- Figure/table expected and delivered counts
- Image pixel dimensions, displayed dimensions, effective ppi, and aspect-ratio deviation
- Inline versus anchored image count
- DOCX and PDF rendered page counts
- Every-page visual inspection status and corrected defects
- Remaining source-limited exceptions

## Final response

State the main DOCX and PDF paths first. Report missing supplements or source limitations briefly. Do not claim perfect layout unless both structural audit and every-page visual review passed.
