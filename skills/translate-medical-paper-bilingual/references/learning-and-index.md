# Glossary-first learning editions and cross-paper review

## One evidence record, multiple outputs

For each source paragraph or caption, store its stable ID, English text, Chinese translation, section, source PDF/page, selected glossary IDs, and figure/table links once. For each glossary entry, store the intact term, wordwise verified IPA, context-specific Chinese meaning, morphology/etymology and examples if justified, source URLs/titles/access dates, and paragraph IDs. Include supplementary material under the same article ID with a `补充材料 S...` source label. Deduplicate verified evidence by term **and sense**, retaining provenance; never merge merely similar gene symbols, receptor names, or progestin/progesterone.

Complete the article/supplement translation and checked glossary before laying out the learning edition. Generate both editions from the same paragraph records, and derive learning blocks only from checked glossary records. Reuse already verified dictionary/etymology results from the shared index. Batch independent lookup where practical, but revisit an ambiguous pronunciation, etymology, meaning, conflicting source, or new context. Token savings never excuse invented IPA, omitted text, or skipped QA.

## Glossary morphology and examples

- Preserve all V2 columns other than the two added after `专业中文`: `词根词缀释义` and `词根词缀举例`. Turn on wrap text; separate each meaningful family/example with a newline inside the cell, not separate spreadsheet columns or one row per word of a phrase.
- Analyze only medically or academically useful word parts. Do not decompose `the` or ordinary phrases such as `growth factors` merely to fill the cells. For `fibroblast`, do not claim that `-blast` alone proves immaturity in every context.
- Group documented variants as `endo-/end-：内、内部` and `metr-/metro-/metra-/metri-：子宫`; mark a documented antonym such as `hypo-：低于正常` and a form such as `形容词 -plastic` only when applicable to the actual entry. Give a few medically relevant **other** examples, each with verified textbook-style IPA, an explicit breakdown and a Chinese translation.
- Example style: `endocardium /ˌendəʊˈkɑ:diəm/ — endo-（内）＋ cardi-（心）——心内膜。` Check pronunciations and morphology before using any example in a final file.
- For a blend or disputed historical coinage, label `词源关联` rather than pretending to mechanically segment the word. For example, *progesterone* is documented as a blend of *progestin* and *Luteosteron*; a separately verified related word may illustrate recall, but must not be presented as the word's literal formation.
- Prefer established medical terminology references (for example NCI/NIH medical dictionaries and reputable medical textbooks) for clinical senses and morphology, and verified learner dictionaries for IPA. Record the exact supporting source in a provenance/note field or internal evidence record. If evidence is insufficient, retain the accurate term/meaning and leave the two morphology cells empty; flag the omission in QC rather than making it up.

## Learning edition blocks

Keep the reading edition unchanged: English paragraph immediately followed by its Chinese translation, without an added learning block. In the learning edition, place `本段英语学习` **after the Chinese translation**, selecting only useful terms actually present in that paragraph. For a caption or table note, place its learning block after the bilingual caption/note without separating the figure from its captions.

Use one rendered line for each selected term and the next rendered line for its useful morphological/etymological note. Example:

**uterus** /ˈju:tərəs/：子宫。  
**uter-**：子宫。例：**intrauterine** /ˌɪntrəˈju:təraɪn/ — intra-（内部）＋ uter-（子宫）——宫内的。  
**progesterone** /prəʊˈdʒestərəʊn/：孕酮。  
**词源关联**：progestin 与 Luteosteron 拼合；相关例词 **gestation** /dʒesˈteɪʃən/ — gest-（与妊娠相关）＋ -ation（过程）——妊娠。

The example illustrates layout, not an exemption from verifying every IPA and etymology in an actual edition. Oxford Advanced Learner's Dictionary documents the blend (`https://www.oxfordlearnersdictionaries.com/definition/english/progesterone`), and Cambridge provides the pronunciation of *gestation* (`https://dictionary.cambridge.org/pronunciation/english/gestation`); confirm the source and medically useful word-part explanation for each real output. If useful morphology is unavailable, give the term/IPA/meaning line alone; do not fabricate a second line. Do not turn a whole paragraph into a glossary dump.

Within one paper, give a term's full explanation on the first pedagogically useful occurrence. If it reappears after a substantial section gap and matters to understanding, give one or two short recall prompts (`先回想词义` followed by IPA and context meaning). Skip adjacent repetitions and never target a fixed count for its own sake. Explain a new sense fully. Across papers, if the user has marked a prior paper as read, use a short recall prompt at the next useful occurrence; expand again for a new sense, long lapse, or a user-marked difficult word. If reading has not been confirmed, do not infer mastery from file generation: explain it fully when needed. Every paper's own glossary remains complete and understandable on its own.

## Shared cross-paper index

Maintain one Excel workbook at `D:\EEC_metabolism\literature\翻译\_shared\跨文献词汇索引.xlsx`, separate from each paper's five official deliverables. Create it on the first **completed** new paper. Merge it automatically once per completed paper, after QA; do not update it on every occurrence or require the user to edit each word. Back up the current workbook before replacing it and record the source edition/version so rerunning the same version is idempotent.

At minimum track a stable term+sense key, full term, verified IPA, Chinese sense, morphology/etymology and examples, evidence citations, first and latest paper/edition, list of paper IDs, last full explanation, last review, ambiguity flags, and optional user-marked `已读/困难/熟悉` state. Preserve manual states and existing verified sources when merging; flag conflicts for inspection. Treat a generated paper as `已制作`, never as proof the user read it or mastered its words. A single user message marking a whole paper `已读` may update its paper-level status, and an explicit difficult/familiar word may override its review schedule; neither is mandatory. Do not rewrite older paper deliverables when the index changes.

If the workbook is missing or unreadable, create/repair a versioned backup and proceed with a fully self-contained per-paper glossary, noting the issue. Do not make a prior index a prerequisite for faithful translation. This index is a reuse/review aid, not a second source of scientific truth: recheck discrepancies against authoritative references.
