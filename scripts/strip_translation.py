#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re

# Devanagari → Western digit map
devanagari_digit_map = str.maketrans('०१२३४५६७८९', '0123456789')

def replace_avarta_numbers(text):
    """Convert 'आवर्तः ७' → 'आवर्तः 007'"""
    match = re.search(r'आवर्तः\s*([०-९]+)', text)
    if match:
        dev_digits = match.group(1)
        western_digits = dev_digits.translate(devanagari_digit_map)
        padded = f"{int(western_digits):03}"
        return re.sub(r'आवर्तः\s*[०-९]+', f'आवर्तः {padded}', text)
    return text

# Load HTML
with open('_site/sagara/publish.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# 1. Remove all divs with class "translation-inline"
for div in soup.find_all("div", class_="translation-inline"):
    div.decompose()

# 2. Update all <h2> tags
for h2 in soup.find_all('h2'):
    if h2.string and 'आवर्तः' in h2.string:
        updated = replace_avarta_numbers(h2.string)
        h2.string.replace_with(updated)

# Save output
with open('_site/sagara/publish_skt.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
