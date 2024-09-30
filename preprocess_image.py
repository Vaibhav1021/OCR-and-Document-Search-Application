# preprocess_image.py

import cv2

def preprocess_image(image_path):
    """
    Preprocess the image to improve OCR accuracy.

    Parameters:
    - image_path: Path to the image file.

    Returns:
    - thresh_img: Preprocessed image.
    """
    img = cv2.imread(image_path)
    
    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding
    _, thresh_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return thresh_img
