# Chapter 20 — Why does deep learning work?

- **Book pages:** 402-420
- **Chapter PDF:** [`chapter-20-why-does-deep-learning-work.pdf`](chapter-20-why-does-deep-learning-work.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#20](https://github.com/majorgilles/understanding-deep-learning-prince/issues/20)

## Focus

Examine optimization, generalization, overparameterization, depth, lottery tickets, and adversarial behavior.

## Learning checkpoint

Evaluate competing explanations for why large deep networks fit and generalize.

## Video lectures

From [Deep Learning Fall 2024](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3), taught by
[Dr. Tamer Elsayed](https://www.youtube.com/channel/UCSYrSQ_eCjw5lL2rP3a5wAg) at Qatar University:

- [Open the complete course playlist](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3)
- No chapter-specific lecture is currently listed in this playlist.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`20_1_Random_Data.ipynb`](notebooks/20_1_Random_Data.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap20/20_1_Random_Data.ipynb) | Official (MIT) |
| [`20_2_Full_Batch_Gradient_Descent.ipynb`](notebooks/20_2_Full_Batch_Gradient_Descent.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap20/20_2_Full_Batch_Gradient_Descent.ipynb) | Official (MIT) |
| [`20_3_Lottery_Tickets.ipynb`](notebooks/20_3_Lottery_Tickets.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap20/20_3_Lottery_Tickets.ipynb) | Official (MIT) |
| [`20_4_Adversarial_Attacks.ipynb`](notebooks/20_4_Adversarial_Attacks.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap20/20_4_Adversarial_Attacks.ipynb) | Official (MIT) |

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
