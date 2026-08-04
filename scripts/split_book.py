"""Split the Understanding Deep Learning PDF according to course_manifest.json."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_pdf", type=Path, help="Path to the complete source PDF")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("course_manifest.json"),
        help="Course manifest containing one-indexed PDF page ranges",
    )
    parser.add_argument(
        "--copy-full-book",
        action="store_true",
        help="Also copy the unchanged source PDF into book/",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_pdf = args.source_pdf.resolve()
    manifest_path = args.manifest.resolve()
    root = manifest_path.parent
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    reader = PdfReader(source_pdf)

    if args.copy_full_book:
        destination = root / manifest["course"]["book_source"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source_pdf != destination.resolve():
            shutil.copy2(source_pdf, destination)

    for chapter in manifest["chapters"]:
        start = chapter["pdf_page_start"]
        end = chapter["pdf_page_end"]
        if not 1 <= start <= end <= len(reader.pages):
            raise ValueError(
                f"Invalid PDF range for chapter {chapter['number']}: {start}-{end}"
            )

        writer = PdfWriter()
        for page_index in range(start - 1, end):
            writer.add_page(reader.pages[page_index])
        writer.add_metadata(
            {
                "/Title": (
                    f"Understanding Deep Learning — Chapter {chapter['number']}: "
                    f"{chapter['title']}"
                ),
                "/Author": manifest["course"]["author"],
                "/Subject": "Noncommercial chapter extract for the follow-along course",
                "/Source": manifest["course"]["website"],
            }
        )

        output = root / chapter["chapter_pdf"]
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("wb") as file:
            writer.write(file)
        print(f"Chapter {chapter['number']}: {output} ({end - start + 1} pages)")


if __name__ == "__main__":
    main()
