# Repository agent guidance

## Educational notes notebooks

Organize chapter notes by **topic**, not as one flat sequence of unrelated sections.

Use this heading and numbering hierarchy:

```text
# Chapter N notes

## Topic 1 — First concept
### 1.1 First explanation
### 1.2 Example
### 1.3 Takeaway

## Topic 2 — Second concept
### 2.1 First explanation
### 2.2 Comparison or example
```

When the discussion moves to a distinct concept, create a new topic and restart its subsection numbering. Keep definitions, derivations, examples, and takeaways beneath the topic they explain; do not continue one global section sequence across unrelated concepts.

Use a **separate Markdown cell for every heading and section**. A topic heading and each numbered subsection must each begin their own cell; never place multiple section headings in one Markdown cell.

Use LaTeX for mathematical notation in notebook Markdown cells rather than formatting formulas as inline code.
