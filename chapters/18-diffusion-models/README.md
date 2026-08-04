# Chapter 18 — Diffusion models

- **Book pages:** 349-373
- **Chapter PDF:** [`chapter-18-diffusion-models.pdf`](chapter-18-diffusion-models.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#18](https://github.com/majorgilles/understanding-deep-learning-prince/issues/18)

## Focus

Model data by learning to reverse a gradual noising process.

## Learning checkpoint

Connect the forward and reverse processes and implement the core one-dimensional diffusion steps.

## Video lectures

From [Deep Learning Fall 2024](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3), taught by
[Dr. Tamer Elsayed](https://www.youtube.com/channel/UCSYrSQ_eCjw5lL2rP3a5wAg) at Qatar University:

- [Open the complete course playlist](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3)
- No chapter-specific lecture is currently listed in this playlist.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`18_1_Diffusion_Encoder.ipynb`](notebooks/18_1_Diffusion_Encoder.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap18/18_1_Diffusion_Encoder.ipynb) | Official (MIT) |
| [`18_2_1D_Diffusion_Model.ipynb`](notebooks/18_2_1D_Diffusion_Model.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap18/18_2_1D_Diffusion_Model.ipynb) | Official (MIT) |
| [`18_3_Reparameterized_Model.ipynb`](notebooks/18_3_Reparameterized_Model.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap18/18_3_Reparameterized_Model.ipynb) | Official (MIT) |
| [`18_4_Families_of_Diffusion_Models.ipynb`](notebooks/18_4_Families_of_Diffusion_Models.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap18/18_4_Families_of_Diffusion_Models.ipynb) | Official (MIT) |

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
