from pypdf import PdfReader
from docx import Document
import os   

def load_pdfs(file_path): 

    documents = []

    reader = PdfReader(file_path)

    for page_num, page in enumerate(reader.pages):

            page_text = (
                page.extract_text() or ""
            )

            if not page_text.strip():
                continue

           

            documents.append(
                {
                    "page_num": page_num + 1,
                    "text": page_text
                }
            )

    return documents

def load_docx(file_path):
     doc = Document(file_path)

     text = ""
     
     for paragraph in doc.paragraphs:
          text += paragraph.text + "\n"
    
     return [
          {
             
            "page_num": 1,
            "text": text  
          }
        ]


def load_txt(file_path):
     
    with open(file_path,
               "r",
               encoding="utf-8") as f:
          text = f.read()

    
    return [
         {
              "page_num": 1,
              "text": text
         }
    ]

def load_documents(folder):
     documents = []

     for filename in os.listdir(folder):
          
          file_path = os.path.join(folder, filename)

          if filename.endswith(".pdf"):
               pages = load_pdfs(file_path)
            
          elif filename.endswith(".docx"):
               pages = load_docx(file_path)

          elif filename.endswith(".txt"): 
               pages = load_txt(file_path)

          else:
            continue
          

          for page in pages:
               documents.append(
                    {
                        "filename": filename,
                        "page_num": page["page_num"],
                        "text": page["text"]
                    }
                )
        
     return documents

               

