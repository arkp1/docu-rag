from app.document_loader import load_documents
from app.vector_store import create_collection
from app.rag import ingest_documents
import time

collection = create_collection()

start = time.time()

documents = load_documents(
    "data/"
)

ingest_documents(
    collection,
    documents
)

print(
    "Ingestion took:",
    time.time() - start
)

print(
    "Collection count:",
    collection.count()
)