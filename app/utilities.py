import os
from tempfile import NamedTemporaryFile
from spire.doc import *
from spire.doc.common import *
from tempfile import gettempdir
from uuid import uuid4
from io import BytesIO



def convert_to_protected_pdf(docx_path):
    document = Document()
    document.LoadFromFile(docx_path)
  

    temp_pdf_path = os.path.join(gettempdir(), f"{uuid4().hex}.pdf")

    try:
       
        document.SaveToFile(temp_pdf_path)

       
        pdf_buffer = BytesIO()
        with open(temp_pdf_path, "rb") as temp_pdf:
            pdf_buffer.write(temp_pdf.read())

        pdf_buffer.seek(0)
        return pdf_buffer

    finally:
      
        document.Close()


        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)
