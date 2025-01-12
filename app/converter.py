import streamlit as st
import app.utilities as utilities
import os
from tempfile import NamedTemporaryFile

def convert_docx_to_pdf(uploaded_file):

    if "pdf_buffer" not in st.session_state:
        st.session_state.pdf_buffer = None

    if "converted" not in st.session_state:
        st.session_state.converted = False

    uploaded_file_name = uploaded_file.name if uploaded_file else "your_file.docx"

   
    if st.button("Convert to PDF"):
  
        with NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            temp_docx_path = temp_file.name

     
        pdf_buffer = utilities.convert_to_protected_pdf(
            temp_docx_path
        )

        os.remove(temp_docx_path)


        st.session_state.pdf_buffer = pdf_buffer
        st.session_state.converted = True

 
    if st.session_state.converted and st.session_state.pdf_buffer:
        st.download_button(
            label="Download PDF",
            data=st.session_state.pdf_buffer,
            file_name=uploaded_file_name.replace(".docx", ".pdf"),
            mime="application/pdf",
        )
