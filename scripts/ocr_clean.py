#!/usr/bin/env python3

import sys

def clean_ocr_text(text):
    # Step-by-step cleaning
    text = text.replace ("|", "।")
    text = text.replace(" ।", "।")
    text = text.replace("। ", "।\n")
    text = text.replace(" -", "")
    text = text.replace("- ", "")
    text = text.replace("-\n", "")
    text = text.replace(":", "ः")  # Replace colon with visarga
    text = text.replace("सिद्धय", "सिद्ध्य")
    text = text.replace("तः करण", "तःकरण")
    text = text.replace("मेद", "भेद")
    return text

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 ocr_clean.py input_file.txt output_file.txt")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as infile:
        raw_text = infile.read()

    cleaned_text = clean_ocr_text(raw_text)

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(cleaned_text)

    print(f"✅ Cleaned text written to: {output_path}")

if __name__ == "__main__":
    main()
