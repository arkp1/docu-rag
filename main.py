from app.pdf_loader import load_pdfs
from app.vector_store import (
    create_collection,
    retrieve
)
from app.rag import ingest_documents
from app.llm import generate_answer


collection = create_collection()

documents = load_pdfs(
    "data/"
)

ingest_documents(
    collection,
    documents
)

while True:
    question = input(
        "Ask your question: "
    )

    results = retrieve(
        collection,
        question
    )

    retrieved_docs = results[
        "documents"
    ][0]

    context = "\n\n".join(
        retrieved_docs
    )

    answer = generate_answer(
        context,
        question
    )

    print(answer)

    sources = {
        metadata["source"]
        for metadata in results[
            "metadatas"
        ][0]
    }

    print("\nSources:\n")

    for source in sources:
        print(source)