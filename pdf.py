from pypdf import PdfReader

def read_pdf(doc):
    pdf = PdfReader(doc)
    pdf_text = ""
    for i, page in enumerate(pdf.pages):
        data = page.extract_text()
        if data:
            pdf
            pdf_text+=data
    return(pdf_text)
