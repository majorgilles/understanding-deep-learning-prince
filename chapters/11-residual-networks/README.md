# Chapter 11 — Residual networks

- **Book pages:** 186-206
- **Chapter PDF:** [`chapter-11-residual-networks.pdf`](chapter-11-residual-networks.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#11](https://github.com/majorgilles/understanding-deep-learning-prince/issues/11)

## Focus

Train deeper systems with residual connections, residual blocks, and batch normalization.

## Learning checkpoint

Explain how residual pathways affect gradients and construct a residual block.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`11_1_Shattered_Gradients.ipynb`](notebooks/11_1_Shattered_Gradients.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap11/11_1_Shattered_Gradients.ipynb) | Official (MIT) |
| [`11_2_Residual_Networks.ipynb`](notebooks/11_2_Residual_Networks.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap11/11_2_Residual_Networks.ipynb) | Official (MIT) |
| [`11_3_Batch_Normalization.ipynb`](notebooks/11_3_Batch_Normalization.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap11/11_3_Batch_Normalization.ipynb) | Official (MIT) |

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
