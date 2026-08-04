# Chapter 12 — Transformers

- **Book pages:** 207-239
- **Chapter PDF:** [`chapter-12-transformers.pdf`](chapter-12-transformers.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#12](https://github.com/majorgilles/understanding-deep-learning-prince/issues/12)

## Focus

Process sequences with tokenization, self-attention, multi-head attention, and transformer architectures.

## Learning checkpoint

Implement self-attention and explain encoder, decoder, and encoder–decoder use cases.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`12_1_Self_Attention.ipynb`](notebooks/12_1_Self_Attention.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap12/12_1_Self_Attention.ipynb) | Official (MIT) |
| [`12_2_Multihead_Self_Attention.ipynb`](notebooks/12_2_Multihead_Self_Attention.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap12/12_2_Multihead_Self_Attention.ipynb) | Official (MIT) |
| [`12_3_Tokenization.ipynb`](notebooks/12_3_Tokenization.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap12/12_3_Tokenization.ipynb) | Official (MIT) |
| [`12_4_Decoding_Strategies.ipynb`](notebooks/12_4_Decoding_Strategies.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap12/12_4_Decoding_Strategies.ipynb) | Official (MIT) |

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
