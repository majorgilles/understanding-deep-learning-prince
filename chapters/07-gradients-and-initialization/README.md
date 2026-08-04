# Chapter 07 — Gradients and initialization

- **Book pages:** 96-117
- **Chapter PDF:** [`chapter-07-gradients-and-initialization.pdf`](chapter-07-gradients-and-initialization.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#7](https://github.com/majorgilles/understanding-deep-learning-prince/issues/7)

## Focus

Compute parameter gradients with backpropagation and initialize networks for stable learning.

## Learning checkpoint

Trace backpropagation through a toy model and justify a sensible initialization strategy.

## Video lectures

From [Deep Learning Fall 2024](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3), taught by
[Dr. Tamer Elsayed](https://www.youtube.com/channel/UCSYrSQ_eCjw5lL2rP3a5wAg) at Qatar University:

- [Lecture 12 | Backpropagation I](https://www.youtube.com/watch?v=NHWP339RnAs)
- [Lecture 13 | Backpropagation II](https://www.youtube.com/watch?v=3pVRMPmqwhc)
- [Lecture 14 | Model Initialization](https://www.youtube.com/watch?v=7RTusO198Bk)

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`7_1_Backpropagation_in_Toy_Model.ipynb`](notebooks/7_1_Backpropagation_in_Toy_Model.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap07/7_1_Backpropagation_in_Toy_Model.ipynb) | Official (MIT) |
| [`7_2_Backpropagation.ipynb`](notebooks/7_2_Backpropagation.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap07/7_2_Backpropagation.ipynb) | Official (MIT) |
| [`7_3_Initialization.ipynb`](notebooks/7_3_Initialization.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap07/7_3_Initialization.ipynb) | Official (MIT) |

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
