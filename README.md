# OCR and Document Search Application

### Overview

This project is an Optical Character Recognition (OCR) web application designed to extract text from images containing Hindi and English text. It provides functionalities for searching keywords within the extracted text and highlighting the occurrences. The application is built using Streamlit, a popular framework for creating web applications in Python.

### Objectives

-Text Extraction: Utilize OCR to extract text from images.
-Keyword Search: Enable users to search for specific keywords in the extracted text.
-Highlighting: Highlight found keywords for easier visibility.
-File Download: Allow users to download the extracted text in JSON or plain text formats.

### Technologies Used

- Python: Programming language used to build the application.
- Streamlit: Framework for creating web applications.
- Pytesseract: OCR tool for text extraction from images.
- OpenCV: Library for image processing.
- Pillow: Library for image handling.
- NumPy: Library for numerical operations.


### Project Structure

ocr_project/
│
├── app.py                  # Main Streamlit application file
├── ocr.py                  # OCR functionality using Pytesseract
├── search_documents.py      # Basic search functionality (for future use)
├── preprocess_image.py      # Optional image preprocessing functions
├── requirements.txt         # Project dependencies
└── assets/                  # Folder containing example images


### Features

1.Image Upload: Users can upload images in PNG, JPG, or JPEG formats.
2.Text Extraction: The application extracts text from the uploaded image using OCR.
3.Keyword Search: Users can enter a keyword to search within the extracted text.
4.Highlighting: The application highlights all occurrences of the searched keyword.
5.Download Extracted Text: Users can download the extracted text as JSON or plain text.

Installation Instructions for Windows
1. Clone the Repository:
git clone https://github.com/yourusername/ocr_project.git
cd ocr_project

2. Set Up a Virtual Environment:
It's recommended to use a virtual environment to manage project dependencies.

#Using venv
python -m venv ocr_env

 #Activate the virtual environment
ocr_env\Scripts\activate 


3. Install Dependencies:
Install the required Python packages:
pip install -r requirements.txt

4. Install Tesseract OCR
Download Tesseract Installer:
- Go to the Tesseract OCR GitHub releases page.
- Download the latest .exe installer (e.g., tesseract-ocr-w64-setup-v5.3.0.exe).

Run the Installer:
- Double-click the downloaded installer.
- Follow the installation steps, making sure to note the installation path (default is C:\Program Files\Tesseract-OCR).


Set Tesseract Path:
- Ensure the installation path is correctly set in ocr.py:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

5. Verify Tesseract Installation:
Run the following command in Command Prompt to ensure Tesseract is installed correctly:
tesseract --version

You should see version information displayed.

### Running the Application

After installing the dependencies and setting up Tesseract, you can run the application using the following command:
streamlit run app.py

This command will start a local web server, and the application will open in your default web browser at http://localhost:8501

### Code Explanation

1. app.py
- Main Application Logic: Handles the user interface, including file uploads, text extraction, keyword search, and downloads.
- User Interaction: Utilizes Streamlit components to create an interactive UI for users.
- 
2. ocr.py
- OCR Functionality: Implements the perform_ocr function to convert uploaded images into text using Pytesseract.
- Image Processing: Converts images to grayscale and applies thresholding to improve OCR accuracy.
  
3. search_documents.py
- Keyword Search: Contains a function to search for keywords in the extracted text, which can be extended to handle multiple documents.
  
4. preprocess_image.py
- Image Preprocessing: Optional functions for preprocessing images before OCR to enhance text extraction quality.

### Testing

- To test the application, upload images containing Hindi and English text.
- Enter a keyword in the search box to find occurrences in the extracted text.
- Download the extracted text in your preferred format.


### Conclusion

This OCR and document search application showcases the integration of various technologies to provide a seamless user experience for text extraction and searching. It serves as a foundation for further enhancements, such as supporting more languages, processing multi-page documents, and improving the UI/UX.
