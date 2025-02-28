import pytesseract
from PIL import Image
import json
import sys
import os

# Ensure Tesseract is installed and configured correctly
TESSERACT_CMD = "/usr/bin/tesseract"  # Adjust path if necessary
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def extract_text(image_path):
    """
    Extracts text from an image using Tesseract OCR.
    :param image_path: Path to the image file.
    :return: Extracted text as a string.
    """
    try:
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img)
        return extracted_text
    except Exception as e:
        return f"Error processing image: {e}"

def process_image(image_path, output_json=True):
    """
    Processes an image, extracts text, and returns structured JSON output.
    :param image_path: Path to the image file.
    :param output_json: Whether to return JSON format.
    :return: Extracted text in structured format.
    """
    extracted_text = extract_text(image_path)
    
    # Structure output as JSON
    result = {
        "image": os.path.basename(image_path),
        "extracted_text": extracted_text.strip()
    }

    if output_json:
        return json.dumps(result, indent=4, ensure_ascii=False)
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ocr_processor.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)

    output = process_image(image_path)
    print(output)
