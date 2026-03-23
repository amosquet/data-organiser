import pymupdf
import pytesseract
from PIL import Image


# Extract text from documents
def doc_extract(file_path: str):

    all_blocks = []
    try:
        with pymupdf.open(file_path) as doc:
            for page in doc:
                all_blocks.extend(page.get_text("blocks"))
        return all_blocks

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return "-1"

    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return "-2"


# Extract text from images
def tesseract_img_extract(file_path: str) -> str:

    try:
        text = pytesseract.image_to_string(Image.open(file_path), timeout=5)
        return text

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return "-1"

    except RuntimeError as timeout_error:
        print(f"An error occurred while reading the img: {timeout_error}")
        print("Tesseract timeout")
        return "-3"
