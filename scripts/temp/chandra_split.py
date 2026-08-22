#!/usr/bin/env python3

import re
import os
import argparse

def devanagari_to_arabic(dev_num):
    devanagari_digits = '०१२३४५६७८९'
    arabic_digits = '0123456789'
    return dev_num.translate(str.maketrans(devanagari_digits, arabic_digits))

def parse_blocks(content):
    blocks = content.strip().split('\n===')
    parsed = []

    for block in blocks:
        lines = block.strip().splitlines()
        if not lines:
            continue

        # First line contains the number and question
        first_line = lines[0].strip()
        match = re.match(r'^([०१२३४५६७८९\.]+)\s+(.*)', first_line)
        if not match:
            print(f"Skipping malformed block:\n{first_line}")
            continue

        full_dev_qnum = match.group(1).rstrip('।.')  # Strip trailing danda or dot
        question_text = match.group(2).strip()

        arabic_qnum = devanagari_to_arabic(full_dev_qnum)
        if '.' in arabic_qnum:
            section_number = arabic_qnum.split('.')[0]
            qnum_hyphen = arabic_qnum.replace('.', '-')
        else:
            section_number = arabic_qnum
            qnum_hyphen = arabic_qnum

        body = '\n'.join(lines[1:]).strip()

        parsed.append((arabic_qnum, qnum_hyphen, question_text, body))

    return parsed

def split_questions(input_file, template, output_dir, kala_number):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = parse_blocks(content)

    for qnum, qnum_hyphen, question_text, body in blocks:
        filename = f"{kala_number}.{qnum}.md"

        output_content = (
            template
            .replace("<<kala_number>>", kala_number)
            .replace("<<question_number>>", qnum)
            .replace("<<question_number_permalink>>", qnum_hyphen)
            .replace("<<question_text_skt>>", question_text)
            .replace("<<body>>", body)
        )

        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(output_content)

        print(f"Written question {qnum} to {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Split questions using === separator and Devanagari question numbers.')
    parser.add_argument('input_filename', help='Path to the input text file.')
    parser.add_argument('template_filename', help='Template file with placeholders.')
    parser.add_argument('output_directory', help='Directory to save output question files.')
    parser.add_argument('kala_number', help='The kala number (e.g., "1").')

    args = parser.parse_args()

    with open(args.template_filename, 'r', encoding='utf-8') as tf:
        template_content = tf.read()

    split_questions(args.input_filename, template_content, args.output_directory, args.kala_number)

if __name__ == "__main__":
    main()
