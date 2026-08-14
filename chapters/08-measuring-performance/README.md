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

## Video lectures

From [Deep Learning Fall 2024](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3), taught by
[Dr. Tamer Elsayed](https://www.youtube.com/channel/UCSYrSQ_eCjw5lL2rP3a5wAg) at Qatar University:

- [Lecture 15 | Measuring Performance I](https://www.youtube.com/watch?v=WQ4yseT2OJQ)
- [Lecture 16 | Measuring Performance II, Regularization I](https://www.youtube.com/watch?v=reEZjWqH8f0)

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`8_1_MNIST_1D_Performance.ipynb`](notebooks/8_1_MNIST_1D_Performance.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap08/8_1_MNIST_1D_Performance.ipynb) | Official (MIT) |
| [`8_2_Bias_Variance_Trade_Off.ipynb`](notebooks/8_2_Bias_Variance_Trade_Off.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap08/8_2_Bias_Variance_Trade_Off.ipynb) | Official (MIT) |
| [`8_3_Double_Descent.ipynb`](notebooks/8_3_Double_Descent.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap08/8_3_Double_Descent.ipynb) | Official (MIT) |
| [`8_4_High_Dimensional_Spaces.ipynb`](notebooks/8_4_High_Dimensional_Spaces.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap08/8_4_High_Dimensional_Spaces.ipynb) | Official (MIT) |
| [`chapter_08_bias_variance_decomposition_from_scratch.ipynb`](notebooks/chapter_08_bias_variance_decomposition_from_scratch.ipynb) | Chapter 8, Section 8.2.2 | Companion: step-by-step bias–variance decomposition |

## Folder contract

- `notebooks/` — official fill-in-the-code exercises and clearly named companion study notebooks.
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
