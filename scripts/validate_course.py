"""Validate the generated course structure and chapter PDF ranges."""

from __future__ import annotations

import json
import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^]]*]\(([^)]+)\)")


def validate_local_links(markdown_file: Path) -> list[str]:
    errors: list[str] = []
    text = markdown_file.read_text(encoding="utf-8")
    for target in MARKDOWN_LINK.findall(text):
        target = target.split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        resolved = (markdown_file.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"Broken link in {markdown_file.relative_to(ROOT)}: {target}")
    return errors


def main() -> None:
    manifest = json.loads((ROOT / "course_manifest.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    official_notebook_count = 0
    all_notebook_count = 0

    if len(manifest["chapters"]) != 21:
        errors.append(f"Expected 21 chapters; found {len(manifest['chapters'])}")

    full_book = ROOT / manifest["course"]["book_source"]
    if not full_book.exists():
        errors.append(f"Missing complete source PDF: {full_book.relative_to(ROOT)}")

    for chapter in manifest["chapters"]:
        workspace = ROOT / chapter["workspace"]
        chapter_pdf = ROOT / chapter["chapter_pdf"]
        expected_pages = chapter["pdf_page_end"] - chapter["pdf_page_start"] + 1

        for required in (workspace / "README.md", workspace / "notes.md", chapter_pdf):
            if not required.exists():
                errors.append(f"Missing required file: {required.relative_to(ROOT)}")

        if chapter_pdf.exists():
            actual_pages = len(PdfReader(chapter_pdf).pages)
            if actual_pages != expected_pages:
                errors.append(
                    f"{chapter_pdf.relative_to(ROOT)} has {actual_pages} pages; "
                    f"expected {expected_pages}"
                )

        notebook_dir = workspace / "notebooks"
        actual_notebooks = sorted(notebook_dir.glob("*.ipynb"))
        official_notebook_count += len(chapter["official_notebooks"])
        all_notebook_count += len(actual_notebooks)
        if not actual_notebooks:
            errors.append(f"Chapter {chapter['number']} has no notebook")

        for notebook in actual_notebooks:
            try:
                parsed = json.loads(notebook.read_text(encoding="utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as error:
                errors.append(f"Invalid notebook {notebook.relative_to(ROOT)}: {error}")
                continue
            if parsed.get("nbformat") != 4 or "cells" not in parsed:
                errors.append(f"Unexpected notebook structure: {notebook.relative_to(ROOT)}")

    for markdown_file in ROOT.rglob("*.md"):
        errors.extend(validate_local_links(markdown_file))

    if official_notebook_count != 68:
        errors.append(f"Expected 68 official notebooks; manifest has {official_notebook_count}")
    if all_notebook_count != 69:
        errors.append(f"Expected 69 total notebooks; found {all_notebook_count}")

    if errors:
        print("Course validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Course validation passed")
    print(f"- Chapters: {len(manifest['chapters'])}")
    print(f"- Official notebooks: {official_notebook_count}")
    print(f"- Total notebooks: {all_notebook_count}")


if __name__ == "__main__":
    main()
