# Chapter 16 — Normalizing flows

- **Book pages:** 304-326
- **Chapter PDF:** [`chapter-16-normalizing-flows.pdf`](chapter-16-normalizing-flows.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#16](https://github.com/majorgilles/understanding-deep-learning-prince/issues/16)

## Focus

Build exact density models from invertible transformations and change-of-variable calculations.

## Learning checkpoint

Compute a transformed density and identify architectural constraints required for invertibility.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`16_1_1D_Normalizing_Flows.ipynb`](notebooks/16_1_1D_Normalizing_Flows.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap16/16_1_1D_Normalizing_Flows.ipynb) | Official (MIT) |
| [`16_2_Autoregressive_Flows.ipynb`](notebooks/16_2_Autoregressive_Flows.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap16/16_2_Autoregressive_Flows.ipynb) | Official (MIT) |
| [`16_3_Contraction_Mappings.ipynb`](notebooks/16_3_Contraction_Mappings.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap16/16_3_Contraction_Mappings.ipynb) | Official (MIT) |

## Folder contract

- `notebooks/` — official fill-in-the-code exercises, except the labeled Chapter 14 study guide.
- `src/` — cleaned code worth retaining after notebook exploration.
- `tests/` — small checks for important behavior and reproducibility.
- `artifacts/` — plots, samples, metrics, and screenshots; generated files stay local by default.

## Deliverables

- [ ] Read the chapter PDF and record questions in `notes.md`.
- [ ] Complete each notebook exercise in order.
- [ ] Move reusable implementations into `src/`.
- [ ] Add focused checks under `tests/`.
- [ ] Save representative results under `artifacts/`.
- [ ] Summarize takeaways, open questions, and gotchas in `notes.md`.
