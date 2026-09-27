# Glossary-first reading edition and cross-paper review

## One evidence record, one reading edition

For each source paragraph or caption, store its stable ID, English text, Chinese translation, section, source PDF/page, selected glossary IDs, matched English/Chinese highlight spans, and figure/table links once. For each glossary entry, store the intact term, wordwise verified IPA, context-specific Chinese meaning, morphology/etymology and examples if justified, source URLs/titles/access dates, and paragraph IDs. Include supplementary material under the same article ID with a `补充材料 S...` source label. Deduplicate verified evidence by term **and sense**, retaining provenance; never merge merely similar gene symbols, receptor names, or progestin/progesterone.

Complete the article/supplement translation and checked glossary before laying out the **single reading edition**. Apply paired yellow-and-underlined term markup directly to the English paragraph and its Chinese translation. Reuse verified dictionary/etymology results from the shared index, but revisit an ambiguous pronunciation, etymology, meaning, conflicting source, or new context. Token savings never excuse invented IPA, omitted terms, or skipped QA.

## Glossary morphology and examples

- Preserve all V2 columns other than the two added after `专业中文`: `词根词缀释义` and `词根词缀举例`. Turn on wrap text; separate each meaningful family/example with a newline inside the cell, not separate spreadsheet columns or one row per word of a phrase.
- Analyze only medically or academically useful word parts. Do not decompose `the` or ordinary phrases such as `growth factors` merely to fill the cells. For `fibroblast`, do not claim that `-blast` alone proves immaturity in every context.
- Group documented variants as `endo-/end-：内、内部` and `metr-/metro-/metra-/metri-：子宫`; mark a documented antonym such as `hypo-：低于正常` and a form such as `形容词 -plastic` only when applicable to the actual entry. Give a few medically relevant **other** examples, each with verified textbook-style IPA, an explicit breakdown and a Chinese translation.
- Example style: `endocardium /ˌendəʊˈkɑ:diəm/ — endo-（内）＋ cardi-（心）——心内膜。` Check pronunciations and morphology before using any example in a final file.
- For a blend or disputed historical coinage, label `词源关联` rather than pretending to mechanically segment the word. For example, *progesterone* is documented as a blend of *progestin* and *Luteosteron*; a separately verified related word may illustrate recall, but must not be presented as the word's literal formation.
- Prefer established medical terminology references (for example NCI/NIH medical dictionaries and reputable medical textbooks) for clinical senses and morphology, and verified learner dictionaries for IPA. Record the exact supporting source in a provenance/note field or internal evidence record. If evidence is insufficient, retain the accurate term/meaning and leave the two morphology cells empty; flag the omission in QC rather than making it up.

## In-text learner support

Keep each English paragraph immediately followed by its Chinese translation; never add a separate learning block. Mark the first relevant occurrence of each selected difficult term in **every paragraph or caption where it matters**, together with its exact Chinese counterpart; one highlighted pair per term per paragraph is enough. Deduplicate only the glossary row, not the occurrence. A recurring word that changes meaning receives a new term+sense record.

Apply the beginner threshold from `translation-standard.md` across all article sections and captions, including terms that a clinician may know in Chinese but not recognize in academic English. A 38-row glossary for a full technical article is a signal to rescreen, not a satisfactory default. Record any zero-highlight paragraph and review it for omissions. Across papers, reuse verified word meanings and IPA in the shared index while keeping each paper's own glossary self-contained. Do not infer mastery from prior document generation; explicit user-marked `已读/困难/熟悉` states may inform review but never remove needed terms from the current paper.

## Shared cross-paper index

Maintain one Excel workbook at `D:\EEC_metabolism\literature\翻译\_shared\跨文献词汇索引.xlsx`, separate from each paper's three official deliverables. Create it on the first **completed** new paper. Merge it automatically once per completed paper, after QA; do not update it on every occurrence or require the user to edit each word. Back up the current workbook before replacing it and record the source edition/version so rerunning the same version is idempotent.

At minimum track a stable term+sense key, full term, verified IPA, Chinese sense, morphology/etymology and examples, evidence citations, first and latest paper/edition, list of paper IDs, last highlighted occurrence, ambiguity flags, and optional user-marked `已读/困难/熟悉` state. Preserve manual states and verified sources when merging; flag conflicts for inspection. Treat a generated paper as `已制作`, never as proof the user read or mastered its words. Do not rewrite older paper deliverables when the index changes.

If the workbook is missing or unreadable, create/repair a versioned backup and proceed with a fully self-contained per-paper glossary, noting the issue. Do not make a prior index a prerequisite for faithful translation. This index is a reuse/review aid, not a second source of scientific truth: recheck discrepancies against authoritative references.
