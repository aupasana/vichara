#!/usr/bin/env python3

import sys
import os

def main():
    if len(sys.argv) != 3:
        print("Usage: python create_avarta_file.py <number> <filename>")
        sys.exit(1)

    number = sys.argv[1]
    filename = sys.argv[2]

    if os.path.exists(filename):
        print(f"File '{filename}' already exists. Nothing done.")
        return

    content = f"""---
layout: layout_avarta
permalink: /sagara/7/{number}
avarta_num: {number}
title: आवर्तः {number}
skip_title: false
draft: true
index_terms: 
---
"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"File '{filename}' created with frontmatter for number {number}.")

if __name__ == "__main__":
    main()
