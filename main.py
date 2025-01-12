import streamlit as st
from app import converter,upload

st.set_page_config(page_title="DOCX to PDF Converter", layout="centered")

def main():
    st.title("DOCX to PDF Converter")
    st.write("Upload a DOCX file, view its metadata, and download the converted PDF.")
    
    file = upload.upload_and_display_metadata()
    
    if file:
       
        converter.convert_docx_to_pdf(file)

if __name__ == "__main__":
    main()
