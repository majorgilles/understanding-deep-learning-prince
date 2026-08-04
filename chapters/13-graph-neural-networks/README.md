# Chapter 13 — Graph neural networks

- **Book pages:** 240-268
- **Chapter PDF:** [`chapter-13-graph-neural-networks.pdf`](chapter-13-graph-neural-networks.pdf)
- **Complete book:** [`../../book/UnderstandingDeepLearning_02_09_26_C.pdf`](../../book/UnderstandingDeepLearning_02_09_26_C.pdf)
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#13](https://github.com/majorgilles/understanding-deep-learning-prince/issues/13)

## Focus

Represent graphs and solve graph- and node-level tasks with message passing and graph attention.

## Learning checkpoint

Implement a graph neural network layer and match graph representations to task-specific losses.

## Video lectures

From [Deep Learning Fall 2024](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3), taught by
[Dr. Tamer Elsayed](https://www.youtube.com/channel/UCSYrSQ_eCjw5lL2rP3a5wAg) at Qatar University:

- [Open the complete course playlist](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3)
- No chapter-specific lecture is currently listed in this playlist.

## Notebooks

| Notebook | Source | Status |
|---|---|---|
| [`13_1_Graph_Representation.ipynb`](notebooks/13_1_Graph_Representation.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap13/13_1_Graph_Representation.ipynb) | Official (MIT) |
| [`13_2_Graph_Classification.ipynb`](notebooks/13_2_Graph_Classification.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap13/13_2_Graph_Classification.ipynb) | Official (MIT) |
| [`13_3_Neighborhood_Sampling.ipynb`](notebooks/13_3_Neighborhood_Sampling.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap13/13_3_Neighborhood_Sampling.ipynb) | Official (MIT) |
| [`13_4_Graph_Attention_Networks.ipynb`](notebooks/13_4_Graph_Attention_Networks.ipynb) | [upstream](https://github.com/udlbook/udlbook/blob/main/Notebooks/Chap13/13_4_Graph_Attention_Networks.ipynb) | Official (MIT) |

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
