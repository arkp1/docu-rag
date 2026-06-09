from app.vector_store import (
    create_collection,
    retrieve
)
from app.llm import generate_answer
from app.query_rewriter import rewrite_query
from app.reranker import rerank

collection = create_collection()

print("RAG document assistant v2" +
      "\n--------------------------")

while True:
    question = input(
        "\nAsk your question: \n"
    )

    if question.lower() in ["exit", "quit"]:
        break

    retrieval_query = rewrite_query(question)
    print("retrieval_query", retrieval_query)

    results = retrieve(
        collection, 
         retrieval_query
    )

    retrieved_docs = results[
        "documents"
    ][0]

    print(
    "\nBefore reranking:",
    len(retrieved_docs)
)

    reranked_docs = rerank(question, retrieved_docs, top_k=5)

    print(
    "After reranking:",
    len(reranked_docs)
)

    context = "\n\n".join(
        reranked_docs
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
    
    print("collection count",collection.count())

