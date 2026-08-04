# Chapter 15 — Generative adversarial networks

- **Book pages:** 276-303
- **Chapter PDF:** [`chapter-15-generative-adversarial-networks.pdf`](chapter-15-generative-adversarial-networks.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#15](https://github.com/majorgilles/understanding-deep-learning-prince/issues/15)

## Focus

Learn generative models through adversarial discrimination and study stability and conditional generation.

## Learning checkpoint

Implement a toy GAN objective and diagnose common training instabilities.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`15_1_GAN_Toy_Example.ipynb`](notebooks/15_1_GAN_Toy_Example.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap15/15_1_GAN_Toy_Example.ipynb) | Official (MIT) |
| [`15_2_Wasserstein_Distance.ipynb`](notebooks/15_2_Wasserstein_Distance.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap15/15_2_Wasserstein_Distance.ipynb) | Official (MIT) |

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
