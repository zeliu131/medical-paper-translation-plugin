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

- Mark complete terms, not arbitrary word fragments.
- Use the same semantic span in both languages.
- Keep markup sparse enough for sustained reading; 60-150 terms is a typical full-paper range, adjusted to article length and learner level.
- Fill the glossary's pronunciation column with verified IPA in `/.../` for English words, including the content words of multiword terms in their original order. Label differing UK and US forms, for example `UK /.../; US /.../`. Check a reputable dictionary's pronunciation entry; for specialized terms, consult a medical dictionary or authoritative pronunciation source. Record the source URL or title in the translation note so the transcription can be audited.
- For gene symbols, receptor abbreviations, chemical formulas, and initialisms, distinguish a verified spoken letter sequence from a spelled-out full name; do not invent a word-like IPA pronunciation. If no reliable pronunciation can be verified, enter `NOT_VERIFIED` and state what was checked and why it remains unresolved. Do not leave a whole column as `NOT_VERIFIED` without attempting verification term by term.
