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

        for page_num, page in enumerate(reader.pages):

            page_text = (
                page.extract_text() or ""
            )

            if not page_text.strip():
                continue

           

            documents.append(
                {
                    "filename": filename,
                    "page_num": page_num + 1,
                    "text": page_text
                }
            )

    return documents