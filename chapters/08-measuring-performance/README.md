# Chapter 08 — Measuring performance

- **Book pages:** 118-137
- **Chapter PDF:** [`chapter-08-measuring-performance.pdf`](chapter-08-measuring-performance.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#8](https://github.com/majorgilles/understanding-deep-learning-prince/issues/8)

## Focus

Measure training and test behavior through error decomposition, bias–variance trade-offs, and double descent.

## Learning checkpoint

Design an evaluation procedure that separates optimization, generalization, and data-related error.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`8_1_MNIST_1D_Performance.ipynb`](notebooks/8_1_MNIST_1D_Performance.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap08/8_1_MNIST_1D_Performance.ipynb) | Official (MIT) |
| [`8_2_Bias_Variance_Trade_Off.ipynb`](notebooks/8_2_Bias_Variance_Trade_Off.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap08/8_2_Bias_Variance_Trade_Off.ipynb) | Official (MIT) |
| [`8_3_Double_Descent.ipynb`](notebooks/8_3_Double_Descent.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap08/8_3_Double_Descent.ipynb) | Official (MIT) |
| [`8_4_High_Dimensional_Spaces.ipynb`](notebooks/8_4_High_Dimensional_Spaces.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap08/8_4_High_Dimensional_Spaces.ipynb) | Official (MIT) |

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
