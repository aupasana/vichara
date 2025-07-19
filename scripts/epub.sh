#!/bin/bash

# Remove divs with translation-inline
#perl -0777 -pe 's{<div[^>]*class\s*=\s*["'\''"]translation-inline["'\''"][^>]*>.*?</div>}{}gs'  _site/sagara/publish.html > _site/sagara/publish_skt.html
./scripts/strip_translation.py

# Convert to epub
pandoc --toc --toc-depth=5 --metadata title="vichara sagara skt" --metadata creator="nischala das" -o _site/sagara/sagara.epub _site/sagara/publish_skt.html

# Show the doc timestamp
ls -la _site/sagara/publish*
ls -la _site/sagara/sagara.epub