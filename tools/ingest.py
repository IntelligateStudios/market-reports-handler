#!/usr/bin/env python3
"""Take a market report PDF into the project.

Reads:  the PDF given on the command line, and every reports/*/report.json (to refuse a PDF already taken).
Writes: reports/<YYYY-MM-DD>-<slug>/ with
          source.pdf        the file, byte for byte
          pages/NNN.txt     each page's text with its layout kept (pdftotext -layout, else pdfplumber)
          pages/NNN.png     each page as a picture, for charts and tables the text loses (pdftoppm, 110 dpi)
          tables/NNN.json   the tables pdfplumber finds on a page, as rows of cells
          report.json       the header: id, file name, sha256, page count, when it was taken

It reads nothing into the ledger. The rankings are read by a person or Claude from pages/ and written to
reports/<id>/rankings.json (schema in README.md); `ledger.py unify` takes them from there.

Usage: python3 -I tools/ingest.py <file.pdf> [--slug <words>] [--date YYYY-MM-DD] [--no-images]
The date is the day the report was received (today, UTC, unless given).
"""
import argparse
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "report"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def already_taken(digest):
    for header in sorted(REPORTS.glob("*/report.json")):
        if json.loads(header.read_text()).get("sha256") == digest:
            return header.parent.name
    return None


def page_texts(pdf, out):
    """One text file per page. Returns the page count."""
    if shutil.which("pdftotext"):
        whole = subprocess.run(
            ["pdftotext", "-layout", str(pdf), "-"], capture_output=True, check=True
        ).stdout.decode("utf-8", "replace")
        pages = whole.split("\f")
        if pages and not pages[-1].strip():
            pages.pop()
    else:
        import pdfplumber

        with pdfplumber.open(pdf) as doc:
            pages = [(p.extract_text() or "") for p in doc.pages]
    for i, text in enumerate(pages, 1):
        (out / f"{i:03d}.txt").write_text(text)
    return len(pages)


def page_tables(pdf, out):
    try:
        import pdfplumber
    except ImportError:
        return 0
    found = 0
    with pdfplumber.open(pdf) as doc:
        for i, page in enumerate(doc.pages, 1):
            tables = [t for t in page.extract_tables() if t and len(t) > 1]
            if tables:
                out.mkdir(exist_ok=True)
                (out / f"{i:03d}.json").write_text(json.dumps(tables, ensure_ascii=False, indent=1))
                found += len(tables)
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pdf")
    ap.add_argument("--slug")
    ap.add_argument("--date")
    ap.add_argument("--no-images", action="store_true")
    args = ap.parse_args()

    pdf = Path(args.pdf)
    if not pdf.is_file():
        sys.exit(f"No such file: {pdf}")
    digest = sha256(pdf)
    taken = already_taken(digest)
    if taken:
        print(f"Already taken as reports/{taken} (same sha256). Nothing written.")
        return

    date = args.date or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    report_id = f"{date}-{slugify(args.slug or pdf.stem)}"
    folder = REPORTS / report_id
    if folder.exists():
        sys.exit(f"reports/{report_id} exists with another file. Give another --slug.")
    (folder / "pages").mkdir(parents=True)
    shutil.copyfile(pdf, folder / "source.pdf")

    count = page_texts(folder / "source.pdf", folder / "pages")
    tables = page_tables(folder / "source.pdf", folder / "tables")
    images = 0
    if not args.no_images and shutil.which("pdftoppm"):
        subprocess.run(
            ["pdftoppm", "-r", "110", "-png", str(folder / "source.pdf"), str(folder / "pages" / "p")],
            check=True,
        )
        for png in sorted((folder / "pages").glob("p-*.png")):
            number = int(png.stem.split("-")[-1])
            png.rename(folder / "pages" / f"{number:03d}.png")
            images += 1

    chars = sum(len(p.read_text().strip()) for p in (folder / "pages").glob("*.txt"))
    header = {
        "id": report_id,
        "file": pdf.name,
        "sha256": digest,
        "bytes": pdf.stat().st_size,
        "pages": count,
        "received": date,
        "taken": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": "taken",
    }
    (folder / "report.json").write_text(json.dumps(header, indent=1) + "\n")
    print(f"reports/{report_id}: {count} pages, {chars} characters of text, {tables} tables, {images} page pictures")
    if count and chars / count < 200:
        print("Little text per page: the report is mostly pictures. Read pages/*.png for the rankings.")
    print(f"Next: read the pages and write reports/{report_id}/rankings.json, then `ledger.py unify {report_id}`.")


if __name__ == "__main__":
    main()
