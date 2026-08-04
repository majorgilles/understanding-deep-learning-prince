# Chapter 10 — Convolutional networks

- **Book pages:** 161-185
- **Chapter PDF:** [`chapter-10-convolutional-networks.pdf`](chapter-10-convolutional-networks.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#10](https://github.com/majorgilles/understanding-deep-learning-prince/issues/10)

## Focus

Use convolution, equivariance, downsampling, and upsampling to process structured spatial data.

## Learning checkpoint

Implement 1D and 2D convolutional operations and reason about their output dimensions.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`10_1_1D_Convolution.ipynb`](notebooks/10_1_1D_Convolution.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap10/10_1_1D_Convolution.ipynb) | Official (MIT) |
| [`10_2_Convolution_for_MNIST_1D.ipynb`](notebooks/10_2_Convolution_for_MNIST_1D.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap10/10_2_Convolution_for_MNIST_1D.ipynb) | Official (MIT) |
| [`10_3_2D_Convolution.ipynb`](notebooks/10_3_2D_Convolution.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap10/10_3_2D_Convolution.ipynb) | Official (MIT) |
| [`10_4_Downsampling_and_Upsampling.ipynb`](notebooks/10_4_Downsampling_and_Upsampling.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap10/10_4_Downsampling_and_Upsampling.ipynb) | Official (MIT) |
| [`10_5_Convolution_For_MNIST.ipynb`](notebooks/10_5_Convolution_For_MNIST.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap10/10_5_Convolution_For_MNIST.ipynb) | Official (MIT) |

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
