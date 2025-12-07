#!/usr/bin/env python3

from bs4 import BeautifulSoup, NavigableString
import re
from weasyprint import HTML

# Devanagari → Western digit map
devanagari_digit_map = str.maketrans('०१२३४५६७८९', '0123456789')

# Load HTML
with open('_site/publish/upanishads_raw.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# 1. Remove all divs with class "translation-inline"
for div in soup.find_all("div", class_="translation-inline"):
    div.decompose()

# Keep text, remove <a> tags
for a in soup.find_all("a"):
    a.unwrap()

footnote_css_inline = "border-left: 1px dashed black; padding-left: 30px;"
# Find all with class "footnote"
for tag in soup.find_all(class_="footnote"):
    # Append or set inline style
    if tag.has_attr("style"):
        tag["style"] += " " + footnote_css_inline
    else:
        tag["style"] = footnote_css_inline

# Regex: * followed by Devanagari or ASCII digits
footnote_pattern = re.compile(r"\*[०-९0-9]+")

# Walk through all text nodes not inside .footnote
for text_node in soup.find_all(string=footnote_pattern):
    # if text_node.find_parent(class_="footnote"):
    #     continue  # skip footnotes

    new_content = []
    last_end = 0
    for match in footnote_pattern.finditer(text_node):
        # Add text before the match
        new_content.append(text_node[last_end:match.start()])

        # Wrap the match in <i>
        i_tag = soup.new_tag("i")
        i_tag.string = f"({match.group()})"
        new_content.append(i_tag)

        last_end = match.end()

    # Add any remaining text
    new_content.append(text_node[last_end:])

    # Replace the original text with new fragments
    text_node.replace_with(*new_content)

# Find all <b> tags and update their style
for b_tag in soup.find_all("strong"):
    # Keep any existing style and append color
    existing_style = b_tag.get("style", "")
    if existing_style and not existing_style.strip().endswith(";"):
        existing_style += ";"
    b_tag["style"] = f'{existing_style} color: darkblue; text-decoration: underline;'

# Mapping: ASCII -> Devanagari
num_map = str.maketrans("0123456789", "०१२३४५६७८९")

# Replace digits in all text nodes
for text_node in soup.find_all(string=True):
    if isinstance(text_node, NavigableString):
        new_text = text_node.translate(num_map)
        if new_text != text_node:
            text_node.replace_with(new_text)

# Save output
with open('_site/publish/upanishads.html', 'w', encoding='utf-8') as f:
    f.write(soup.decode())

HTML("_site/publish/upanishads.html").write_pdf("_site/publish/upanishads.pdf")