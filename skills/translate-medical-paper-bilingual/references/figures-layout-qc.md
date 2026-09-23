# Figure Extraction, Placement, and Visual QA

## Extraction order

1. Inspect the PDF with `pdfinfo`, `pdfimages -list`, and rendered pages.
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

## Final visual inspection

- Render every DOCX page and every final PDF page to PNG.
- Inspect at 100% zoom and zoom further for dense figures.
- Confirm figure order, caption order, page association, panel completeness, axis readability, table alignment, and absence of clipping or overlap.
- Compare figure count and labels against the source article and the article's in-text references.
- A contact sheet is useful for global order but never replaces inspection of individual pages.
