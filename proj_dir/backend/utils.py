import pdfplumber
from docx import Document
from io import BytesIO

def extract_pdf_text(file):
    with pdfplumber.open(BytesIO(file.read())) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages])

def extract_docx_text(file):
    doc = Document(BytesIO(file.read()))
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

def extract_txt_text(file):
    return file.read().decode('utf-8')