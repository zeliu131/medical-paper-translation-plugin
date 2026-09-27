# Figure Extraction, Placement, and Visual QA

## Extraction order

1. Inspect the main PDF and each verified supplementary PDF independently with `pdfinfo`, `pdfimages -list`, and rendered pages. Enumerate figures, **every panel and its outermost content**, tables, captions, source pages, and supplement identifiers before layout. Keep a full-page original screenshot for each source figure.
2. Prefer a native embedded image **only after** verifying it contains the entire composite, including vector-drawn labels and separate panel objects, at adequate resolution. A single PDF image object often contains only part of a composite figure.
3. If a figure is assembled from several PDF objects or vector elements, render the full page at 300-400 dpi and crop the **entire** figure region. Use source-page-specific coordinates and padding beyond the outermost left/right/top/bottom labels; never assume the figure is centered.
4. Compare the original figure, the extracted asset, and the final rendered DOCX/PDF side by side for **each figure ID**. Check all panel letters, axes, tick labels, gene names, row names, legends, insets, scale bars, brackets, significance marks, and the leftmost/rightmost/topmost/bottommost text. Preserve comparison images and a per-figure pass/fail checklist in `work_records`.
5. Save losslessly as PNG unless the source is photographic and JPEG is materially smaller without visible loss.

## Crop rules

- Include the entire scientific figure and nothing from adjacent body text or caption. Leave a small clean margin around the outermost content. A label touching a crop edge or cut at the left or bottom is a failed crop, even when the plot itself seems readable.
- Never crop by guessed fixed coordinates across pages.
- Never use a screenshot of the *previous generated edition* as the figure source. Re-extract from the original article PDF or the publisher's original complete figure, recording source and figure ID.
- Preserve the original aspect ratio. Do not stretch to fill page width.
- If a dense figure cannot fit legibly on an A4 portrait page, give it a dedicated landscape page or full-width page. Do not solve fit by cutting margins or panels. Keep the bilingual caption associated with the complete figure; if it must continue, label the continuation clearly without cutting the graphic.
- If source quality is poor, keep the best available image and record a source-limited warning; do not use AI upscaling to invent labels.

## DOCX placement

- Insert every figure as a `wp:inline` object. Floating `wp:anchor` objects are forbidden because they can shift between Word and PDF renderers.
- Center the figure and choose an intentional physical width.
- Keep the figure and both captions as a single pagination unit where possible; a long caption may continue only after the complete figure and its English start are visible.
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

- Append the translated supplement after the main article and references in the single reading edition; retain its original section, figure/table identifiers and order. Do not append untranslated raw PDF pages in place of bilingual content.
- Preserve each original composite figure at the best fidelity available from its PDF. Follow it with its English caption and complete Chinese caption, including panel legends, scale-bar text, abbreviations and notes. Translate supplementary tables and footnotes without silently changing numbers.
- If original-page appearance itself is needed to audit a complex page, add an original-page image in the work records; do not let it replace selectable English/Chinese text in the two editions.
- Keep English/Chinese terminology markup visible in captions and table notes too; never allow a highlighted translation to separate a caption from its figure.

## Final visual inspection

- Render every DOCX page and every final PDF page to PNG.
- Inspect at 100% zoom and zoom further for dense figures.
- Confirm figure order, caption order, page association, panel completeness, axis readability, table alignment, and absence of clipping or overlap.
- Do a four-edge audit for every original-versus-output figure pair. Explicitly record `left`, `right`, `top`, and `bottom` as pass/fail; review the full rendered PDF page as well as the embedded DOCX media. For a composite such as Fig. 1, compare panel and label inventory with the publisher's original figure, not only with the extracted asset. Any cut axis label, missing row name, truncated legend, missing panel, or cut bottom plot is a release blocker; re-extract and re-render after correction.
- Compare figure count and labels separately against the source article and every verified supplement, including their in-text references.
- A contact sheet is useful for global order but never replaces inspection of individual pages.
