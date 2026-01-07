#!/usr/bin/env python3

import re
import os
import argparse

def devanagari_to_arabic(dev_num):
    devanagari_digits = '०१२३४५६७८९'
    arabic_digits = '0123456789'
    translation_table = str.maketrans(devanagari_digits, arabic_digits)
    return dev_num.translate(translation_table)

def split_sections(input_file, template, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove headers like "===== filename ====="
    content = re.sub(r"^=====.*?=====\n?", "", content, flags=re.MULTILINE)

    # Match only section headers with exactly 3 Devanagari digits inside ()
    pattern = re.compile(r"\(\s*([०१२३४५६७८९]{3})\s*\)(.*?)(?=(\(\s*[०१२३४५६७८९]{3}\s*\))|$)", re.DOTALL)
    sections = pattern.findall(content)

    for dev_section_number, body, _ in sections:
        section_number = devanagari_to_arabic(dev_section_number.strip())
        cleaned_body = body.strip()

        output_content = template.replace("<<section>>", section_number).replace("<<body>>", cleaned_body)

        output_file = os.path.join(output_dir, f"vs_7_{section_number}.md")
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write(output_content)

        print(f"Written section {section_number} to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Split sections marked by 3-digit Devanagari numerals.')
    parser.add_argument('input_filename', help='Path to the input OCR text file.')
    parser.add_argument('template_filename', help='Path to the template file with <<section>> and <<body>>.')
    parser.add_argument('output_directory', help='Directory to save output section files.')

    args = parser.parse_args()

    with open(args.template_filename, 'r', encoding='utf-8') as tf:
        template_content = tf.read()

    split_sections(args.input_filename, template_content, args.output_directory)

if __name__ == "__main__":
    main()
