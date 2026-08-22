#!/usr/bin/env python3

import sys
import re

# --- Devanagari digit mapping ---
def to_devanagari(num):
    devanagari_digits = '०१२३४५६७८९'
    return ''.join(devanagari_digits[int(d)] for d in str(num))

# --- Main script ---
def main():
    if len(sys.argv) != 4:
        print("Usage: python extract_and_replace.py input.txt 44 output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    n = int(sys.argv[2])
    output_file = sys.argv[3]

    start_marker = f"({to_devanagari(n)})"
    end_marker = f"({to_devanagari(n + 1)})"

    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Extract content between markers
    pattern = re.compile(re.escape(start_marker) + r'(.*?)' + re.escape(end_marker), re.DOTALL)
    match = pattern.search(text)

    if not match:
        print(f"Could not find text between {start_marker} and {end_marker}")
        sys.exit(1)

    extracted = match.group(1).strip()
    extracted = start_marker + extracted + end_marker  # Include the markers

    # Read output file and find last '---'
    with open(output_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    yaml_end_idx = None
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == '---':
            yaml_end_idx = i
            break

    if yaml_end_idx is None:
        print("YAML frontmatter separator '---' not found.")
        sys.exit(1)

    # Keep lines up to and including the last '---'
    new_lines = lines[:yaml_end_idx + 1] + ['\n', extracted + '\n']

    # Overwrite output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"Output file '{output_file}' updated with extracted text after YAML frontmatter.")

if __name__ == "__main__":
    main()
