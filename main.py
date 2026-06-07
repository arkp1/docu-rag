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

print("RAG document assistant v2" +
      "\n--------------------------")

while True:
    question = input(
        "\nAsk your question: \n"
    )

    if question.lower() in ["exit", "quit"]:
        break

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

    print("\n" + answer)

    sources = {
        metadata["source"]
        for metadata in results[
            "metadatas"
        ][0]
    }

    print("\nRetrieved Context:\n")

    for i, (doc, metadata) in enumerate(
        zip(
            results["documents"][0],
            results["metadatas"][0]
        ),
        start=1
    ):
        print(f"[{i}] Source: {metadata['source']} (Page: {metadata['page_num']})")

