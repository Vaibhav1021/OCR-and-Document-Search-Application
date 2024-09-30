# ocr.py

import cv2
from PIL import Image
import numpy as np
import pytesseract

# Set Tesseract path (for local setup)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

def perform_ocr(uploaded_file):
    """
    Perform OCR on the uploaded image file.

    Parameters:
    - uploaded_file: Uploaded file object from Streamlit.

    Returns:
    - extracted_text: The text extracted from the image.
    """
    try:
        # Convert the file-like object to an image using PIL
        img = Image.open(uploaded_file)

        # Convert PIL image to OpenCV format
        img_cv = np.array(img)

        # If image has an alpha channel, remove it
        if img_cv.shape[-1] == 4:
            img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGBA2RGB)

        # Convert to grayscale
        gray_img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

        # Optional: Preprocessing steps to improve OCR accuracy
        # You can adjust the threshold value or use adaptive thresholding
        _, thresh_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Perform OCR with English and Hindi languages
        extracted_text = pytesseract.image_to_string(thresh_img, lang='eng+hin')

        return extracted_text
    except Exception as e:
        return f"An error occurred during OCR processing: {e}"

if __name__ == "__main__":
    image_path = "C:/Users/Vaibhav/Desktop/ocr/assets/1.png"
    text = perform_ocr(image_path)
    print(text)
