#!/usr/bin/env python3

import sys
import os
from google.cloud import translate_v2 as translate

def translate_text(text, target_language="en"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/skt-ocr.json")
    translate_client = translate.Client()
    result = translate_client.translate(
        text,
        target_language=target_language,
        format_="text"
    )
    return result["translatedText"]

def main():
    if len(sys.argv) != 3:
        print("Usage: python translate_text.py <input_text_file> <output_translated_file>")
        sys.exit(1)

    input_file = os.path.expanduser(sys.argv[1])
    output_file = os.path.expanduser(sys.argv[2])

    if not os.path.exists(input_file):
        print(f"❌ Error: Input file '{input_file}' does not exist.")
        sys.exit(1)

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()

        print("🌐 Translating text...")
        translated_text = translate_text(text, target_language="en")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(translated_text)

        print(f"🌍 Translated output written to '{output_file}'.")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
