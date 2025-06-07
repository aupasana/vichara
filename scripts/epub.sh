#!/bin/bash

# Remove divs with translation-inline
perl -0777 -pe 's{<div[^>]*class\s*=\s*["'\''"]translation-inline["'\''"][^>]*>.*?</div>}{}gs'  _site/sagara/publish.html > _site/sagara/publish_skt.html

# Convert to epub
pandoc --toc --toc-depth=5 -o _site/sagara/sagara.epub _site/sagara/publish_skt.html
#pandoc --toc --toc-depth=5 -o _site/sagara/sagara.md _site/sagara/publish_skt.html
#pandoc --toc --toc-depth=5 -o _site/sagara/sagara2.epub -o _site/sagara/sagara.md

# pandoc _site/sagara/publish.html -f html -t markdown -o _site/sagara/publish.md
# pandoc _site/sagara/publish.md -o _site/sagara/sagara.epub --toc --toc-depth=5

# Show the doc timestamp
ls -la _site/sagara/sagara.epub