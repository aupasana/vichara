#!/bin/bash

# Remove divs with translation-inline
#perl -0777 -pe 's{<div[^>]*class\s*=\s*["'\''"]translation-inline["'\''"][^>]*>.*?</div>}{}gs'  _site/sagara/publish.html > _site/sagara/publish/raw.html
./scripts/format_sagara_for_epub.py

# Convert to epub
pandoc --toc --toc-depth=5 --metadata title="संस्कृत विचार सागरः" --metadata creator="निश्चल दासः" -o _site/sagara/sagara.epub _site/sagara/publish/raw2.html

# pandoc _site/sagara/publish/raw2.html -o _site/sagara/sagara.pdf --pdf-engine=xelatex -V mainfont="Adishila SemiBold"

# Show the doc timestamp
ls -la _site/sagara/publish*
ls -la _site/sagara/sagara.epub
ls -la _site/sagara/publish/sagara.pdf

