# app.py

import streamlit as st
from ocr import perform_ocr
from PIL import Image
import json
import os
import re

st.set_page_config(page_title="OCR and Search Application", layout="wide")

st.title("📄 OCR and Document Search Application")

# Sidebar for additional options
st.sidebar.header("Settings")
download_option = st.sidebar.selectbox(
    "Download Extracted Text As:",
    ("JSON", "Plain Text")
)

# File uploader
uploaded_file = st.file_uploader("📂 Upload an image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Perform OCR on the uploaded file
    with st.spinner("🔍 Performing OCR..."):
        ocr_text = perform_ocr(uploaded_file)
    
    # Display the extracted text
    st.subheader("📝 Extracted Text")
    st.text_area("", ocr_text, height=300)

    # Save the extracted text to a file
    extracted_text_json = {"extracted_text": ocr_text}
    extracted_text_plain = ocr_text

    # Keyword search functionality with highlighting
    st.subheader("🔍 Search Within Text")
    search_query = st.text_input("Enter keyword to search")

    if search_query:
        with st.spinner("🔎 Searching..."):
            # Use regex for case-insensitive and whole word matching
            pattern = re.compile(re.escape(search_query), re.IGNORECASE)
            matches = list(pattern.finditer(ocr_text))
        
        if matches:
            st.success(f"✅ Keyword '{search_query}' found {len(matches)} time(s) in the text!")

            # Highlight all occurrences of the search query
            highlighted_text = pattern.sub(lambda m: f"**{m.group(0)}**", ocr_text)
            st.markdown("**Highlighted Text:**")
            st.markdown(highlighted_text)
        else:
            st.warning(f"⚠️ Keyword '{search_query}' not found.")

    # Download button for extracted text
    st.subheader("💾 Download Extracted Text")
    if download_option == "JSON":
        json_data = json.dumps(extracted_text_json, ensure_ascii=False, indent=4)
        st.download_button(
            label="Download as JSON",
            data=json_data,
            file_name="extracted_text.json",
            mime="application/json"
        )
    else:
        st.download_button(
            label="Download as Text",
            data=extracted_text_plain,
            file_name="extracted_text.txt",
            mime="text/plain"
        )
