# Figure Extraction, Placement, and Visual QA

## Extraction order

1. Inspect the main PDF and each verified supplementary PDF independently with `pdfinfo`, `pdfimages -list`, and rendered pages. Enumerate figures, panels, tables, captions, source pages, and supplement identifiers before layout.
2. Prefer a native embedded image only when it contains the complete composite figure at adequate resolution.
3. If a figure is assembled from several PDF objects or vector elements, render the full page at 300-400 dpi and crop the complete figure region.
4. Compare the crop with the source page. Confirm all panel letters, axes, tick labels, legends, insets, scale bars, brackets, and significance marks.
5. Save losslessly as PNG unless the source is photographic and JPEG is materially smaller without visible loss.

## Crop rules

- Include the entire scientific figure and nothing from adjacent body text or caption.
- Never crop by guessed fixed coordinates across pages.
- Preserve the original aspect ratio. Do not stretch to fill page width.
- If source quality is poor, keep the best available image and record a source-limited warning; do not use AI upscaling to invent labels.

## DOCX placement

- Insert every figure as a `wp:inline` object. Floating `wp:anchor` objects are forbidden because they can shift between Word and PDF renderers.
- Center the figure and choose an intentional physical width.
- Keep the figure and both captions as a single pagination unit where possible.
- Use `keep_with_next` on the image paragraph and English caption.
- If the full block does not fit, add a page break before the figure; never shrink a detailed plot until labels become unreadable.
- Put one English caption followed by one Chinese caption directly under the same image.

## Resolution rules

- Compute effective ppi from source pixels divided by displayed inches.
- Target: at least 220 ppi.
- Conditional pass: 150-219 ppi only when the source is limiting and all labels are legible at 100% zoom in the final rendered page.
- Fail: below 150 ppi, broken relationship, missing dimensions, or aspect-ratio deviation above 2%.

## Tables

- Prefer a native table for translated content so text remains searchable.
- Repeat header rows across pages and prohibit splitting a patient/data row across pages.
- Use visible but light borders, deliberate column widths, sufficient padding, and readable font size.
- Keep an original table image when it materially helps verify values, but do not force readers to rely on a blurry screenshot.

## Supplementary material

- Append the translated supplement after the main article and references in both editions; retain its original section, figure/table identifiers and order. Do not append untranslated raw PDF pages in place of bilingual content.
- Preserve each original composite figure at the best fidelity available from its PDF. Follow it with its English caption and complete Chinese caption, including panel legends, scale-bar text, abbreviations and notes. Translate supplementary tables and footnotes without silently changing numbers.
- If original-page appearance itself is needed to audit a complex page, add an original-page image in the work records; do not let it replace selectable English/Chinese text in the two editions.
- In the learning edition only, keep any learning block after the complete bilingual caption or table note. Check that the additional block cannot separate figure and captions or cause clipping; reflow/page-break the block as a unit when necessary.

## Final visual inspection

- Render every DOCX page and every final PDF page to PNG.
- Inspect at 100% zoom and zoom further for dense figures.
- Confirm figure order, caption order, page association, panel completeness, axis readability, table alignment, and absence of clipping or overlap.
- Compare figure count and labels separately against the source article and every verified supplement, including their in-text references.
- A contact sheet is useful for global order but never replaces inspection of individual pages.
