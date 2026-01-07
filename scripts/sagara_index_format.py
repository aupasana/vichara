#!/usr/bin/env python3

import sys
import re

# Mapping from Devanagari digits to Arabic digits
devanagari_digit_map = {
    '०': '0', '१': '1', '२': '2', '३': '3', '४': '4',
    '५': '5', '६': '6', '७': '7', '८': '8', '९': '9'
}

def devanagari_to_arabic(dev_num):
    """Convert Devanagari numeral string to Arabic numeral string"""
    return ''.join(devanagari_digit_map.get(ch, ch) for ch in dev_num)

# Read piped input from stdin
for line in sys.stdin:
    # Remove only the newline
    line_content = line.rstrip('\n')

    # Capture trailing spaces (if any) after visible characters
    match_trailing = re.match(r'^(.*?)(\s*)$', line_content)
    core_text, trailing_spaces = match_trailing.groups()

    # Match Devanagari-starting lines
    match = re.match(r'^([०१२३४५६७८९]+)\s+(.*)', core_text)
    if match:
        dev_num = match.group(1)
        rest_text = match.group(2)
        arabic_num = int(devanagari_to_arabic(dev_num))
        formatted_num = f"{arabic_num:03d}"
        print(f"[{core_text}](/sagara/7/{formatted_num}){trailing_spaces}")
    else:
        print(line_content + trailing_spaces)
