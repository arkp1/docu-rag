from app.chunker import create_chunks
from app.vector_store import store_chunks

def ingest_documents(
    collection,
    documents
):

    for doc in documents:

        chunks = create_chunks(
            doc["text"]
        )

        store_chunks(
            collection,
            chunks,
            doc["filename"],
            doc["page_num"]
        )