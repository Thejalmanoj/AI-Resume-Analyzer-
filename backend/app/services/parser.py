from pypdf import PdfReader
from docx import Document


def parse_pdf(file_path):

    text=""

    pdf=PdfReader(file_path)

    for page in pdf.pages:

        content=page.extract_text()

        if content:
            text+=content

    return text


def parse_docx(file_path):

    doc=Document(file_path)

    text=[]

    for para in doc.paragraphs:

        text.append(para.text)

    return "\n".join(text)