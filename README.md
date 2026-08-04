# Understanding Deep Learning — Follow-Along Course

A chapter-by-chapter, noncommercial study repository for [*Understanding Deep Learning*](https://udlbook.github.io/udlbook/) by Simon J. D. Prince. It combines an offline chapter PDF, the official coding notebooks, structured notes, and an actionable GitHub issue for each of the book's 21 chapters.

> This independent course is not endorsed by the author or MIT Press. See [Attribution and provenance](NOTICE.md) and [Licensing](#licensing).

## What is included

- The complete, unchanged February 8, 2026 [book PDF](book/UnderstandingDeepLearning_02_09_26_C.pdf).
- One mechanically extracted PDF per chapter, using the PDF's own bookmarks and page ranges.
- All **68 notebooks linked from the official website**, copied unchanged from the upstream repository at commit [`0d84a591362f`](https://github.com/udlbook/udlbook/commit/0d84a591362f1cc99c6dc2ce1c2544d559280681).
- Chapter-matched links to Dr. Tamer Elsayed's [Deep Learning Fall 2024 video lectures](https://www.youtube.com/playlist?list=PLRdABJkXXytCz19PsZ1PCQBKoZGV069k3).
- One original Chapter 14 study-guide notebook because the official collection has no Chapter 14 notebook.
- Per-chapter notes, source/test/artifact folders, and one GitHub issue per chapter.

## Setup

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
uv sync
uv run jupyter lab
```

Some official notebooks contain their own install or download cells. Review those cells before running them. PyTorch installation details can vary by operating system and accelerator; use the [PyTorch installation selector](https://pytorch.org/get-started/locally/) when you need a CUDA- or ROCm-specific build.

## Suggested workflow

1. Open the chapter's GitHub issue and use it as the completion checklist.
2. Read the chapter PDF and capture questions in `notes.md`.
3. Work through the notebooks in order, filling in the missing code.
4. Move reusable code into `src/`, checks into `tests/`, and representative results into `artifacts/`.
5. Summarize takeaways and close the issue.

## Chapters

Book-page numbers below are the printed page numbers. Each extracted PDF starts at page 1 in most PDF readers.

| Chapter | Topic | Book pages | Chapter PDF | Notebooks | Notes | Issue |
|---:|---|---:|---|---|---|---|
| 01 | [Introduction](chapters/01-introduction/README.md) | 1-16 | [PDF](chapters/01-introduction/chapter-01-introduction.pdf) | [1 official](chapters/01-introduction/notebooks/) | [Notes](chapters/01-introduction/notes.md) | [#1](https://github.com/majorgilles/understanding-deep-learning-prince/issues/1) |
| 02 | [Supervised learning](chapters/02-supervised-learning/README.md) | 17-24 | [PDF](chapters/02-supervised-learning/chapter-02-supervised-learning.pdf) | [1 official](chapters/02-supervised-learning/notebooks/) | [Notes](chapters/02-supervised-learning/notes.md) | [#2](https://github.com/majorgilles/understanding-deep-learning-prince/issues/2) |
| 03 | [Shallow neural networks](chapters/03-shallow-neural-networks/README.md) | 25-40 | [PDF](chapters/03-shallow-neural-networks/chapter-03-shallow-neural-networks.pdf) | [4 official](chapters/03-shallow-neural-networks/notebooks/) | [Notes](chapters/03-shallow-neural-networks/notes.md) | [#3](https://github.com/majorgilles/understanding-deep-learning-prince/issues/3) |
| 04 | [Deep neural networks](chapters/04-deep-neural-networks/README.md) | 41-55 | [PDF](chapters/04-deep-neural-networks/chapter-04-deep-neural-networks.pdf) | [3 official](chapters/04-deep-neural-networks/notebooks/) | [Notes](chapters/04-deep-neural-networks/notes.md) | [#4](https://github.com/majorgilles/understanding-deep-learning-prince/issues/4) |
| 05 | [Loss functions](chapters/05-loss-functions/README.md) | 56-76 | [PDF](chapters/05-loss-functions/chapter-05-loss-functions.pdf) | [3 official](chapters/05-loss-functions/notebooks/) | [Notes](chapters/05-loss-functions/notes.md) | [#5](https://github.com/majorgilles/understanding-deep-learning-prince/issues/5) |
| 06 | [Fitting models](chapters/06-fitting-models/README.md) | 77-95 | [PDF](chapters/06-fitting-models/chapter-06-fitting-models.pdf) | [5 official](chapters/06-fitting-models/notebooks/) | [Notes](chapters/06-fitting-models/notes.md) | [#6](https://github.com/majorgilles/understanding-deep-learning-prince/issues/6) |
| 07 | [Gradients and initialization](chapters/07-gradients-and-initialization/README.md) | 96-117 | [PDF](chapters/07-gradients-and-initialization/chapter-07-gradients-and-initialization.pdf) | [3 official](chapters/07-gradients-and-initialization/notebooks/) | [Notes](chapters/07-gradients-and-initialization/notes.md) | [#7](https://github.com/majorgilles/understanding-deep-learning-prince/issues/7) |
| 08 | [Measuring performance](chapters/08-measuring-performance/README.md) | 118-137 | [PDF](chapters/08-measuring-performance/chapter-08-measuring-performance.pdf) | [4 official](chapters/08-measuring-performance/notebooks/) | [Notes](chapters/08-measuring-performance/notes.md) | [#8](https://github.com/majorgilles/understanding-deep-learning-prince/issues/8) |
| 09 | [Regularization](chapters/09-regularization/README.md) | 138-160 | [PDF](chapters/09-regularization/chapter-09-regularization.pdf) | [5 official](chapters/09-regularization/notebooks/) | [Notes](chapters/09-regularization/notes.md) | [#9](https://github.com/majorgilles/understanding-deep-learning-prince/issues/9) |
| 10 | [Convolutional networks](chapters/10-convolutional-networks/README.md) | 161-185 | [PDF](chapters/10-convolutional-networks/chapter-10-convolutional-networks.pdf) | [5 official](chapters/10-convolutional-networks/notebooks/) | [Notes](chapters/10-convolutional-networks/notes.md) | [#10](https://github.com/majorgilles/understanding-deep-learning-prince/issues/10) |
| 11 | [Residual networks](chapters/11-residual-networks/README.md) | 186-206 | [PDF](chapters/11-residual-networks/chapter-11-residual-networks.pdf) | [3 official](chapters/11-residual-networks/notebooks/) | [Notes](chapters/11-residual-networks/notes.md) | [#11](https://github.com/majorgilles/understanding-deep-learning-prince/issues/11) |
| 12 | [Transformers](chapters/12-transformers/README.md) | 207-239 | [PDF](chapters/12-transformers/chapter-12-transformers.pdf) | [4 official](chapters/12-transformers/notebooks/) | [Notes](chapters/12-transformers/notes.md) | [#12](https://github.com/majorgilles/understanding-deep-learning-prince/issues/12) |
| 13 | [Graph neural networks](chapters/13-graph-neural-networks/README.md) | 240-268 | [PDF](chapters/13-graph-neural-networks/chapter-13-graph-neural-networks.pdf) | [4 official](chapters/13-graph-neural-networks/notebooks/) | [Notes](chapters/13-graph-neural-networks/notes.md) | [#13](https://github.com/majorgilles/understanding-deep-learning-prince/issues/13) |
| 14 | [Unsupervised learning](chapters/14-unsupervised-learning/README.md) | 269-275 | [PDF](chapters/14-unsupervised-learning/chapter-14-unsupervised-learning.pdf) | [1 study guide](chapters/14-unsupervised-learning/notebooks/) | [Notes](chapters/14-unsupervised-learning/notes.md) | [#14](https://github.com/majorgilles/understanding-deep-learning-prince/issues/14) |
| 15 | [Generative adversarial networks](chapters/15-generative-adversarial-networks/README.md) | 276-303 | [PDF](chapters/15-generative-adversarial-networks/chapter-15-generative-adversarial-networks.pdf) | [2 official](chapters/15-generative-adversarial-networks/notebooks/) | [Notes](chapters/15-generative-adversarial-networks/notes.md) | [#15](https://github.com/majorgilles/understanding-deep-learning-prince/issues/15) |
| 16 | [Normalizing flows](chapters/16-normalizing-flows/README.md) | 304-326 | [PDF](chapters/16-normalizing-flows/chapter-16-normalizing-flows.pdf) | [3 official](chapters/16-normalizing-flows/notebooks/) | [Notes](chapters/16-normalizing-flows/notes.md) | [#16](https://github.com/majorgilles/understanding-deep-learning-prince/issues/16) |
| 17 | [Variational autoencoders](chapters/17-variational-autoencoders/README.md) | 327-348 | [PDF](chapters/17-variational-autoencoders/chapter-17-variational-autoencoders.pdf) | [3 official](chapters/17-variational-autoencoders/notebooks/) | [Notes](chapters/17-variational-autoencoders/notes.md) | [#17](https://github.com/majorgilles/understanding-deep-learning-prince/issues/17) |
| 18 | [Diffusion models](chapters/18-diffusion-models/README.md) | 349-373 | [PDF](chapters/18-diffusion-models/chapter-18-diffusion-models.pdf) | [4 official](chapters/18-diffusion-models/notebooks/) | [Notes](chapters/18-diffusion-models/notes.md) | [#18](https://github.com/majorgilles/understanding-deep-learning-prince/issues/18) |
| 19 | [Reinforcement learning](chapters/19-reinforcement-learning/README.md) | 374-401 | [PDF](chapters/19-reinforcement-learning/chapter-19-reinforcement-learning.pdf) | [5 official](chapters/19-reinforcement-learning/notebooks/) | [Notes](chapters/19-reinforcement-learning/notes.md) | [#19](https://github.com/majorgilles/understanding-deep-learning-prince/issues/19) |
| 20 | [Why does deep learning work?](chapters/20-why-does-deep-learning-work/README.md) | 402-420 | [PDF](chapters/20-why-does-deep-learning-work/chapter-20-why-does-deep-learning-work.pdf) | [4 official](chapters/20-why-does-deep-learning-work/notebooks/) | [Notes](chapters/20-why-does-deep-learning-work/notes.md) | [#20](https://github.com/majorgilles/understanding-deep-learning-prince/issues/20) |
| 21 | [Deep learning and ethics](chapters/21-deep-learning-and-ethics/README.md) | 421-436 | [PDF](chapters/21-deep-learning-and-ethics/chapter-21-deep-learning-and-ethics.pdf) | [2 official](chapters/21-deep-learning-and-ethics/notebooks/) | [Notes](chapters/21-deep-learning-and-ethics/notes.md) | [#21](https://github.com/majorgilles/understanding-deep-learning-prince/issues/21) |

## Repository layout

```text
.
├── book/                         # complete, unchanged source PDF
├── chapters/
│   └── NN-topic/
│       ├── README.md             # chapter goal, links, and deliverables
│       ├── chapter-NN-topic.pdf  # chapter-only reading
│       ├── notes.md              # learner-owned notes template
│       ├── notebooks/            # official notebook(s), or Ch. 14 study guide
│       ├── src/                  # stable code extracted from experiments
│       ├── tests/                # reproducibility and behavior checks
│       └── artifacts/            # local outputs; ignored except .gitkeep
├── scripts/                      # split and validation utilities
├── course_manifest.json          # normalized chapter/source metadata
└── pyproject.toml                # uv/Jupyter environment
```

## Rebuilding the chapter PDFs

```bash
uv run python scripts/split_book.py path/to/UnderstandingDeepLearning.pdf --copy-full-book
uv run python scripts/validate_course.py
```

The manifest records one-indexed physical PDF ranges as well as printed book pages.

## Licensing

This is a mixed-license repository:

- The book and chapter extracts: **CC BY-NC-ND 4.0**, copyright Simon J. D. Prince / MIT Press.
- Official notebooks: **MIT**, copyright 2023 Simon Prince.
- Original course scaffolding and Chapter 14 notebook: **MIT**.

See [`LICENSE`](LICENSE), [`LICENSES/`](LICENSES/), and [`book/README.md`](book/README.md) for the scoped notices. The book material may not be used commercially.
