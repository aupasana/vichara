#!/usr/bin/env python3

import sys
import os
import subprocess
from google.cloud import vision

def main():
    if len(sys.argv) != 2:
        print("Usage: python ocr_image.py <page_number>")
        sys.exit(1)

    page_number = sys.argv[1].zfill(3)  # Pads to 3 digits, e.g., '35' → '035'

    # Define paths
    input_path = os.path.expanduser(f"~/ocr/vs_pages/vc-{page_number}.jpg")
    output_path = os.path.expanduser(f"~/ocr/vs-{page_number}-ocr.txt")

    if not os.path.exists(input_path):
        print(f"❌ Error: Input file '{input_path}' does not exist.")
        sys.exit(1)

    # Set the path to your service account key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/skt-ocr.json")

    # Initialize Vision client
    client = vision.ImageAnnotatorClient()

    with open(input_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    image_context = vision.ImageContext(
        language_hints=["sa"]  # 'sa' = Sanskrit, 'hi' = Hindi,
    )

    response = client.document_text_detection(image=image, image_context=image_context)
    annotations = response.full_text_annotation

    if response.error.message:
        print(f"❌ OCR failed: {response.error.message}")
        sys.exit(1)

    ocr_text = annotations.text if annotations.text else ""

    if ocr_text.strip():
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(ocr_text)
        print(f"✅ OCR complete. Output written to '{output_path}'.")

         # Call the cleaning script
        clean_script_path = os.path.join(os.path.dirname(__file__), "ocr_clean.py")
        cleaned_output_path = os.path.expanduser(f"~/ocr/vs-{page_number}-ocr-clean.txt")

        try:
            subprocess.run(
                ["python3", clean_script_path, output_path, cleaned_output_path],
                check=True
            )
            print(f"🧹 Cleaned OCR output written to '{cleaned_output_path}'.")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Error running clean script: {e}")

    else:
        print("⚠️ OCR completed but no text was detected.")

if __name__ == "__main__":
    main()
