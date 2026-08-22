#!/usr/bin/env python3
"""Export snippet cards from _site/ to images.

Harvests the card markup Jekyll already built, wraps it in a minimal page
with the site stylesheet, and renders it through WeasyPrint. Jekyll stays the
only thing that renders markdown, so an exported card cannot drift from the
browsable page at /snippets/...

Requires a prior `jekyll build`. Run via `make snippets`.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml
from bs4 import BeautifulSoup
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / '_snippets'
SITE_DIR = ROOT / '_site'
SITE_CSS = SITE_DIR / 'assets' / 'main.css'

# pdftoppm rasterises at this DPI; WeasyPrint maps 1 CSS px to 1/96 inch, so
# 96 gives a 1:1 pixel match with the card's CSS dimensions.
CSS_DPI = 96

# .snippet-stage breaks the fixed-width card out of minima's centred wrapper,
# which is browser-only chrome — on a page sized to the card it would shove
# everything off-canvas. The shadow is likewise for screen viewing.
EXPORT_CSS = """
@page {{ size: {width}px {height}px; margin: 0; }}
html, body {{ margin: 0; padding: 0; background: #fff; }}
.snippet-stage {{ position: static; left: auto; width: auto; margin: 0; }}
.snippet-card {{ box-shadow: none; }}
"""

PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="{css_uri}">
<style>{export_css}</style>
</head><body>{card}</body></html>
"""


def front_matter(md_path):
    """Return the YAML front matter of a markdown file as a dict."""
    text = md_path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return {}
    _, fm, _ = text.split('---', 2)
    return yaml.safe_load(fm) or {}


def card_size(css_text):
    """Read the card's dimensions out of the compiled stylesheet.

    Keeps the sass the single source of truth for geometry — resizing the
    card in _base.scss changes the export with no edit here.
    """
    block = re.search(r'\.snippet-card\s*\{([^}]*)\}', css_text)
    if not block:
        sys.exit('Could not find .snippet-card in %s' % SITE_CSS)
    dims = {}
    for prop in ('width', 'height'):
        match = re.search(r'\b%s:\s*(\d+)px' % prop, block.group(1))
        if not match:
            sys.exit('.snippet-card has no %s' % prop)
        dims[prop] = int(match.group(1))
    return dims['width'], dims['height']


def harvest(page_path):
    """Pull div.snippet-card out of a built page, with local asset paths.

    Absolute URLs (/assets/images/...) are rewritten to file: URIs under
    _site so WeasyPrint resolves them against the build rather than the
    filesystem root.
    """
    soup = BeautifulSoup(page_path.read_text(encoding='utf-8'), 'html.parser')
    card = soup.find('div', class_='snippet-card')
    if card is None:
        sys.exit('No .snippet-card found in %s' % page_path)

    for tag in card.find_all(['img', 'source']):
        src = tag.get('src')
        if src and src.startswith('/'):
            local = SITE_DIR / src.lstrip('/')
            if not local.exists():
                print('  warning: missing asset %s' % src, file=sys.stderr)
            tag['src'] = local.as_uri()

    return str(card)


def to_png(pdf_path, png_path):
    subprocess.run(
        ['pdftoppm', '-png', '-r', str(CSS_DPI), '-singlefile',
         str(pdf_path), str(png_path.with_suffix(''))],
        check=True)


def to_jpeg(png_path, jpg_path, quality):
    subprocess.run(
        ['magick', str(png_path), '-quality', str(quality), str(jpg_path)],
        check=True)


def export(md_path, out_dir, width, height, css_uri, fmt, quality, keep_pdf):
    meta = front_matter(md_path)
    permalink = meta.get('permalink')
    if not permalink:
        print('  skipped %s (no permalink)' % md_path.name)
        return None

    # a permalink without a trailing slash builds to <path>.html, with one to
    # <path>/index.html
    base = SITE_DIR / permalink.strip('/')
    for candidate in (base.with_suffix('.html'), base / 'index.html'):
        if candidate.exists():
            page_path = candidate
            break
    else:
        sys.exit('%s not built — run `jekyll build` first (looked for %s)'
                 % (md_path.name, base.with_suffix('.html')))

    page = PAGE.format(
        css_uri=css_uri,
        export_css=EXPORT_CSS.format(width=width, height=height),
        card=harvest(page_path))

    out_dir.mkdir(parents=True, exist_ok=True)
    stem = md_path.stem
    pdf_path = out_dir / (stem + '.pdf')
    png_path = out_dir / (stem + '.png')

    HTML(string=page, base_url=str(SITE_DIR)).write_pdf(pdf_path)
    to_png(pdf_path, png_path)

    written = [png_path]
    if fmt in ('jpeg', 'both'):
        jpg_path = out_dir / (stem + '.jpg')
        to_jpeg(png_path, jpg_path, quality)
        written.append(jpg_path)
        if fmt == 'jpeg':
            png_path.unlink()
            written.remove(png_path)

    if not keep_pdf:
        pdf_path.unlink()

    for path in written:
        print('  %s (%.0f KB)' % (path.relative_to(ROOT),
                                  path.stat().st_size / 1024))
    return written


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('names', nargs='*',
                        help='snippet stems to export, e.g. vs_0001 '
                             '(default: all)')
    parser.add_argument('--out', default='exports/snippets',
                        help='output directory (default: exports/snippets)')
    parser.add_argument('--format', choices=['png', 'jpeg', 'both'],
                        default='png', help='output format (default: png)')
    parser.add_argument('--quality', type=int, default=92,
                        help='JPEG quality (default: 92)')
    parser.add_argument('--keep-pdf', action='store_true',
                        help='keep the intermediate PDF')
    args = parser.parse_args()

    for tool in ('pdftoppm',) + (('magick',) if args.format != 'png' else ()):
        if not shutil.which(tool):
            sys.exit('%s not found on PATH' % tool)

    if not SITE_CSS.exists():
        sys.exit('%s missing — run `jekyll build` first' % SITE_CSS)

    sources = sorted(SOURCE_DIR.rglob('*.md'))
    if args.names:
        wanted = set(args.names)
        sources = [p for p in sources if p.stem in wanted]
        missing = wanted - {p.stem for p in sources}
        if missing:
            sys.exit('No such snippet: %s' % ', '.join(sorted(missing)))
    if not sources:
        sys.exit('No snippets found under %s' % SOURCE_DIR)

    width, height = card_size(SITE_CSS.read_text(encoding='utf-8'))
    css_uri = SITE_CSS.as_uri()
    out_dir = (ROOT / args.out) if not Path(args.out).is_absolute() \
        else Path(args.out)

    print('Exporting %d snippet(s) at %dx%d' % (len(sources), width, height))
    for md_path in sources:
        print('%s:' % md_path.stem)
        export(md_path, out_dir, width, height, css_uri,
               args.format, args.quality, args.keep_pdf)


if __name__ == '__main__':
    main()
