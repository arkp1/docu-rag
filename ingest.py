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

# print("SCRIPT STARTED")

# from app.document_loader import load_documents
# from app.vector_store import create_collection
# from app.rag import ingest_documents
# import time

# print("1")

# collection = create_collection()

# print("2")

# start = time.time()

# documents = load_documents(
#     "data/"
# )

# print("3")
# print(f"Loaded {len(documents)} documents")

# ingest_documents(
#     collection,
#     documents
# )

# print("4")

# print(
#     "Ingestion took:",
#     time.time() - start
# )

# print(
#     "Collection count:",
#     collection.count()
# )