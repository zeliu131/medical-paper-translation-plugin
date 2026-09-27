# Biomedical English-Chinese Translation Standard

## Fidelity

- Translate the complete scientific meaning, including uncertainty, comparison groups, timing, dose, and limitations.
- Keep numerical values, units, mathematical symbols, P values, confidence intervals, gene/protein capitalization, and citation numbers unchanged.
- Preserve distinctions such as response versus survival, association versus prediction, and prediction versus treatment effect.
- Do not silently correct a suspected source error. Reproduce it faithfully and explain it in separate translator notes.

## Preferred biomedical phrasing

- Use standard Chinese clinical and pathology terminology rather than literal word order.
- Translate `progestin` according to context as `孕激素类药物` or `合成孕激素`; reserve `孕酮` for progesterone.
- Distinguish a gene symbol such as `PGR` from its protein/receptor product `PR`.
- Translate `patient-derived organoid` as `患者来源类器官` and retain the source abbreviation.
- Translate `cell viability` as `细胞活力` unless the assay specifically establishes survival.
- Translate `vehicle control`, `biological replicate`, and `technical replicate` as `溶剂对照`, `生物学重复`, and `技术重复`.

## Evidential verbs

| English | Default Chinese | Do not inflate to |
| --- | --- | --- |
| may / might | 可能 | 证明 |
| suggest | 提示 | 证实 |
| potential | 潜在的 | 确定的 |
| associate with | 与……相关 | 导致 |
| predict | 预测 | 造成 |
| hypothesize / propose | 提出假设 / 提出 | 已阐明 |
| synergistic | 协同的 | 已完成正式协同检验 |

## Paragraph pairing

- Assign each source paragraph a stable ID such as `S03-P007`.
- Store the English source and Chinese translation in the same content record.
- Emit English first and Chinese second from that record; never pair them manually after layout.
- Count and compare English and Chinese blocks before release.

## Learning markup

- Set the threshold for a clinical/pathology beginner reading biomedical English: include specialized nouns and collocations, methods/statistics phrases, consequential general academic verbs/adjectives, and words needed to understand the article's comparisons, conclusions, or figure captions. Include terms such as `mutational burden`, `formalin-fixed paraffin-embedded`, `propensity score matching`, `susceptibility`, and `exposome` when present; also mark an everyday-looking word if its scientific use is not obvious. Leave elementary function words and transparent repeated words alone. Split a multiword entry only when its parts have separate useful senses; otherwise mark the **whole phrase**.
- Screen every paragraph, heading, figure legend, table heading, and table note rather than taking terms only from the abstract or a machine-generated shortlist. Mark the first useful occurrence of each selected term in **every paragraph or caption in which it matters**; for a repeated term in the same paragraph, one paired highlight is enough. Do not restrict marking to the first occurrence of a major section. Deduplicate glossary rows by term and sense, not in-text highlights.
- The former 60-150-term full-paper range was only a guide, not an upper limit. With the lower beginner threshold, 80-200 distinct terms may be reasonable for a standard full-length biomedical article, and a long technical article can require more. Never pad a glossary to hit a count, cap it at 200, or release a full article with around 38 entries without a documented paragraph-by-paragraph rescreen and an explanation of why no other terms block comprehension.
- Mark complete English terms and the **corresponding complete Chinese expression**, not arbitrary fragments or a nearby unrelated Chinese word. For every selected term occurrence, apply both pale-yellow highlighting and underlining to the English span and the Chinese span in the reading DOCX. If word order or translation changes, explicitly map the exact Chinese span to the English term. Keep gene symbols and abbreviations as written when translation would be misleading; highlight the matching symbol and the translated descriptive phrase where applicable.
- Store **every** translated paragraph/caption in a machine-readable JSON manifest with `paragraphs: [{"id":"S01-P001","english":"full English paragraph","chinese":"完整中文段落","terms":[{"id":"term-sense-id","glossary_id":"row-id","english":"surface form","chinese":"对应中文"}]}]`. Use an empty `terms` array for a paragraph intentionally without highlights. Run `scripts/audit_paired_markup.py` against the reading DOCX and this manifest: it checks that each paragraph pair exists in source order and each English/Chinese term has an explicit pale-yellow highlight and underline. Compare the manifest's paragraph/term counts with the source-content manifest and glossary. Before release, visually verify both colors and underlines in the exported PDF, and inspect every zero-highlight paragraph for omissions. A missing pair, unmatched counterpart, or invisible PDF markup blocks delivery.
- Fill every glossary pronunciation cell with one verified **textbook-style broad IPA** transcription in `/.../`, using the familiar 48-sound chart taught in Chinese English classes. Prefer a reputable British learner dictionary for a consistent reference accent, without requiring both UK and US variants. Use `:` for vowel length (`/i:/`, `/ɑ:/`, `/ɔ:/`, `/u:/`, `/ɜ:/`) and the familiar textbook vowels/diphthongs such as `/ɪ/`, `/e/`, `/əʊ/`, `/ɪə/`, `/eə/`; retain primary/secondary stress (`ˈ`, `ˌ`) and word boundaries. Example: `teacher` `/ˈti:tʃə/`, `patient` `/ˈpeɪʃənt/`. A standard learner-dictionary `/ˈtiːtʃə/` may be displayed as `/ˈti:tʃə/` after a purely typographic length-mark change; do not automatically convert an American pronunciation to a British one or alter vowel quality by search-and-replace.
- Avoid narrow-phonetic or unfamiliar specialized symbols/diacritics when a verified broad textbook transcription exists (for example, choose a verified British learner form instead of automatically rendering an American rhotic `/ɚ/` or `/ɝ/`). Never force an actual pronunciation into the 48-sound chart when this would change the sound. The chart is a learning aid, not a license to invent phonemes; stress marks and combinations such as `/tʃ/` remain necessary. Do not use Chinese character homophones or English respelling as the IPA value. Show a compact symbol key with the glossary (at least `:`, `ˈ`, `ˌ`, `/ə/`, `/ɜ:/`, `/ʃ/`, `/θ/`, `/ð/`, `/ŋ/`) and use a font that renders them correctly in XLSX and PDF.
- Retain the original V2 glossary layout, inserting exactly two columns immediately after `专业中文`: `来源章节 | 英文术语 | 词性/类型 | 发音 | 专业中文 | 词根词缀释义 | 词根词缀举例 | 通俗中文解释 | 原文例句 | ...`. Preserve the order of all remaining V2 columns. Put the **entire English term** in the one `英文术语` cell and put all pronunciations in the one `发音` cell on the same row. For a phrase, give one independently verified `/.../` transcription per written word, including articles such as `the`, in the term's order. Join them with the Chinese punctuation character `、`, without spaces, for example `the uterine stroma` → `/ðə/、/[verified uterine pronunciation]/、/[verified stroma pronunciation]/`. These bracketed placeholders are instructions only; never deliver placeholders. Never create `Word 1`, `IPA 1`, etc. columns, separate phrase terms into several rows, or wrap a whole phrase in just one slash pair. After stripping surrounding punctuation, compare the number and order of whitespace-separated words to the number and order of slash-delimited pronunciation parts. Treat hyphenated compounds as one written unit unless the verified pronunciation explicitly requires component treatment. Verify the last pronunciation matches the last English word: `epithelium` must receive its own pronunciation, never `stroma`'s.
- In both new morphology cells, put one useful family or example on each line, using in-cell newlines and text wrapping. Group genuine allomorphs, e.g. `metr-/metro-/metra-/metri-：子宫`, and label opposites or adjective/noun variants explicitly. Give each example as `medical term /verified IPA/ — prefix/root/suffix（meaning）＋...——专业中文释义`. Source medical morphology and example meanings from reliable medical dictionaries, terminology references, textbooks, or primary educational sources; record URLs and access dates in audit records. Distinguish a documented etymological blend from a productive prefix/root construction. Do not invent an etymology or force ordinary function words and transparent everyday phrases into morphology cells. If there is no justified useful analysis, leave the morphology cells empty, not the pronunciation cell; keep the term and its meaning in the glossary.
- For gene symbols, receptor abbreviations, chemical formulas, and initialisms, use a documented spoken form where available or verified IPA letter names for English letters; label letter-by-letter reading separately from a pronounced full name. Cite the dictionary or pronunciation source URL/title in a source/note column for audit. If no reliable textbook-compatible pronunciation can be verified for **any** word in a term, omit the whole term from the learning glossary and list its name and reason in the QC notes. Never leave a blank or `NOT_VERIFIED` pronunciation cell in a delivered glossary. Before release, inspect a rendered sample of pronunciation cells to ensure no missing glyphs or substituted symbols.
