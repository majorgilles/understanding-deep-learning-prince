# Chapter 05 — Loss functions

- **Book pages:** 56-76
- **Chapter PDF:** [`chapter-05-loss-functions.pdf`](chapter-05-loss-functions.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#5](https://github.com/majorgilles/understanding-deep-learning-prince/issues/5)

## Focus

Derive practical regression and classification losses from maximum likelihood.

## Learning checkpoint

Choose and implement an appropriate loss for regression, binary classification, and multiclass classification.

## Video lectures

From [Deep Learning Fall 2024](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3), taught by
[Dr. Tamer Elsayed](https://www.youtube.com/channel/UCSYrSQ_eCjw5lL2rP3a5wAg) at Qatar University:

- [Lecture 7 | Loss Functions I](https://www.youtube.com/watch?v=5mXp8dr-ROU)
- [Lecture 8 | Loss Functions II](https://www.youtube.com/watch?v=S1xShuO7Z-0)
- [Lecture 9 | Loss Functions III](https://www.youtube.com/watch?v=j-xEfGShu3I)

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`5_1_Least_Squares_Loss.ipynb`](notebooks/5_1_Least_Squares_Loss.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap05/5_1_Least_Squares_Loss.ipynb) | Official (MIT) |
| [`5_2_Binary_Cross_Entropy_Loss.ipynb`](notebooks/5_2_Binary_Cross_Entropy_Loss.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap05/5_2_Binary_Cross_Entropy_Loss.ipynb) | Official (MIT) |
| [`5_3_Multiclass_Cross_entropy_Loss.ipynb`](notebooks/5_3_Multiclass_Cross_entropy_Loss.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap05/5_3_Multiclass_Cross_entropy_Loss.ipynb) | Official (MIT) |

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
