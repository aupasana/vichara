#!/bin/bash

# Remove divs with translation-inline
#perl -0777 -pe 's{<div[^>]*class\s*=\s*["'\''"]translation-inline["'\''"][^>]*>.*?</div>}{}gs'  _site/sagara/publish.html > _site/sagara/publish/raw.html
./scripts/format_sagara_for_epub.py
./scripts/format_upanishads_for_epub.py

pandoc --toc --toc-depth=5 --css=assets/kindle.css --metadata title="संस्कृत विचार सागरः" --metadata creator="निश्चल दासः" -o _site/publish/sagara.epub _site/publish/sagara_souped.html
pandoc --toc --toc-depth=5 --css=assets/kindle.css --metadata title="उपनिषन्मणिप्रभा" --metadata creator="अमर दासः" -o _site/publish/upanishads.epub _site/publish/upanishads_souped.html

# Show the doc timestamp
ls -la _site/publish*

