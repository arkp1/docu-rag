from pypdf import PdfReader
import os

def load_pdfs(pdf_folder):

    documents = []

    for filename in os.listdir(pdf_folder):

        if not filename.endswith(".pdf"):
            continue

        pdf_path = os.path.join(
            pdf_folder,
            filename
        )

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        documents.append(
            {
                "filename": filename,
                "text": text
            }
        )

    return documents