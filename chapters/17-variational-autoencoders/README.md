# Chapter 17 — Variational autoencoders

- **Book pages:** 327-348
- **Chapter PDF:** [`chapter-17-variational-autoencoders.pdf`](chapter-17-variational-autoencoders.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#17](https://github.com/majorgilles/understanding-deep-learning-prince/issues/17)

## Focus

Train latent-variable models with variational inference, the ELBO, and reparameterized gradients.

## Learning checkpoint

Derive the VAE training objective and implement the reparameterization trick.

## Video lectures

From [Deep Learning Fall 2024](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3), taught by
[Dr. Tamer Elsayed](https://www.youtube.com/channel/UCSYrSQ_eCjw5lL2rP3a5wAg) at Qatar University:

- [Open the complete course playlist](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3)
- No chapter-specific lecture is currently listed in this playlist.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`17_1_Latent_Variable_Models.ipynb`](notebooks/17_1_Latent_Variable_Models.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap17/17_1_Latent_Variable_Models.ipynb) | Official (MIT) |
| [`17_2_Reparameterization_Trick.ipynb`](notebooks/17_2_Reparameterization_Trick.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap17/17_2_Reparameterization_Trick.ipynb) | Official (MIT) |
| [`17_3_Importance_Sampling.ipynb`](notebooks/17_3_Importance_Sampling.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap17/17_3_Importance_Sampling.ipynb) | Official (MIT) |

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
