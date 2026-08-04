"""Render course documentation from course_manifest.json.

This script only creates missing chapter README and notes files unless --force is used, so
learner notes are not overwritten accidentally.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated docs")
    return parser.parse_args()


def write_document(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        print(f"Skipped existing {path.relative_to(ROOT)}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {path.relative_to(ROOT)}")


def render_chapter_readme(chapter: dict, repo: str, course: dict) -> str:
    number = chapter["number"]
    chapter_pdf = f"chapter-{number}-{chapter['slug']}.pdf"
    full_book = "../../book/UnderstandingDeepLearning_02_09_26_C.pdf"
    issue_url = f"{repo}/issues/{chapter['issue']}"
    official = chapter["official_notebooks"]
    rows: list[str] = []
    for name in official:
        source = (
            "https://github.com/udlbook/udlbook/blob/main/Notebooks/"
            f"Chap{number}/{name}"
        )
        rows.append(
            f"| [`{name}`](notebooks/{name}) | [upstream]({source}) | Official (MIT) |"
        )
    if not rows:
        name = "14_1_Unsupervised_Learning_Study_Guide.ipynb"
        rows.append(
            f"| [`{name}`](notebooks/{name}) | This repository | "
            "Original study guide (MIT) |"
        )
    notebook_note = ""
    if not official:
        notebook_note = "\n> The official UDL site currently links no notebook for Chapter 14.\n"

    playlist = course["video_playlist"]
    video_links = [
        f"- [{lecture['title']}]({lecture['url']})" for lecture in chapter["video_lectures"]
    ]
    if not video_links:
        video_links = [
            f"- [Open the complete course playlist]({playlist['url']})",
            "- No chapter-specific lecture is currently listed in this playlist.",
        ]
    video_section = "\n".join(video_links)

    return f"""# Chapter {number} — {chapter['title']}

- **Book pages:** {chapter['book_pages']}
- **Chapter PDF:** [`{chapter_pdf}`]({chapter_pdf})
- **Complete book:** [`{full_book}`]({full_book})
- **Course website:** <https://udlbook.github.io/udlbook/>
- **Notes:** [`notes.md`](notes.md)
- **GitHub issue:** [#{chapter['issue']}]({issue_url})

## Focus

{chapter['focus']}

## Learning checkpoint

{chapter['checkpoint']}

## Video lectures

From [{playlist['title']}]({playlist['url']}), taught by
[{playlist['instructor']}]({playlist['channel_url']}) at {playlist['institution']}:

{video_section}

## Notebooks

| Notebook | Source | Status |
|---|---|---|
{chr(10).join(rows)}
{notebook_note}
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
"""


def render_notes(chapter: dict, repo: str) -> str:
    number = chapter["number"]
    chapter_pdf = f"chapter-{number}-{chapter['slug']}.pdf"
    return f"""# Chapter {number} notes — {chapter['title']}

- **Reading:** [`{chapter_pdf}`]({chapter_pdf}), book pages {chapter['book_pages']}
- **Workspace guide:** [`README.md`](README.md)
- **Issue:** [#{chapter['issue']}]({repo}/issues/{chapter['issue']})

## Reading checklist

- [ ] Read the chapter once for structure.
- [ ] Revisit equations, diagrams, and worked examples.
- [ ] Complete the associated notebook exercises.

## Key concepts

-

## Equations and notation

-

## Notebook observations

-

## Questions and gotchas

-

## Takeaways

-
"""


def main() -> None:
    args = parse_args()
    manifest = json.loads((ROOT / "course_manifest.json").read_text(encoding="utf-8"))
    course = manifest["course"]
    repo = course["repository"]
    for chapter in manifest["chapters"]:
        workspace = ROOT / chapter["workspace"]
        write_document(
            workspace / "README.md",
            render_chapter_readme(chapter, repo, course),
            args.force,
        )
        write_document(workspace / "notes.md", render_notes(chapter, repo), args.force)


if __name__ == "__main__":
    main()
