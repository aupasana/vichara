#!/usr/bin/env python3

import re
import os
import yaml

# Function to convert Arabic numerals to Devanagari
def to_devanagari(num_str):
    devanagari_digits = '०१२३४५६७८९'
    return ''.join(devanagari_digits[int(d)] if d.isdigit() else d for d in num_str)

# Load the markdown file containing the links
INPUT_FILE = "index_sagara.md"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Match patterns like: [label](/sagara/3/110)
pattern = re.compile(r'\[([^\]]+?)\]\(/sagara/(\d+)/(\d+)\)')
matches = pattern.findall(content)

for label, vol, num in matches:
    devanagari_num = to_devanagari(num)
    filename = f"./_sagara/{vol}/vs_{vol}_{num}.md"

    if not os.path.exists(filename):
        print(f"⚠️  File not found: {filename}")
        continue

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find YAML frontmatter
    if lines[0].strip() != '---':
        print(f"⚠️  YAML frontmatter not found in {filename}")
        continue

    yaml_end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == '---'), None)
    if yaml_end is None:
        print(f"⚠️  YAML end marker not found in {filename}")
        continue

    yaml_content = ''.join(lines[1:yaml_end])
    data = yaml.safe_load(yaml_content) or {}

    # Clean the label by stripping number prefix
    label_stripped = label.strip()
    devanagari_prefix = to_devanagari(num)
    label_cleaned = re.sub(rf'^({num}|{devanagari_prefix})\s*', '', label_stripped).strip()

    # Construct the new title
    if not label_cleaned:
        new_title = f"आवर्तः {devanagari_num}"
    else:
        new_title = f"आवर्तः {devanagari_num} -- {label_cleaned}"

    data['title'] = new_title

    # Dump YAML and write new file
    new_yaml = yaml.dump(data, allow_unicode=True, sort_keys=False).strip()
    new_lines = ['---\n'] + [line + '\n' for line in new_yaml.splitlines()] + ['---\n'] + lines[yaml_end+1:]

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"✅ Updated: {filename}")

print("🎉 Done.")
