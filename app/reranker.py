from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(question, documents, top_k=5):

    pairs = []

    for document in documents:
        pairs.append((question, document))

    scores = model.predict(pairs, batch_size=8)
    
    ranked = sorted(
                    zip(documents, scores),
                    key=lambda x:x[1],
                    reverse=True)
    
    print("Rerankers scores ")
    for document, score in ranked[:5]:
        print(
        f"\nScore: {score:.4f}"
    )
    return [document for document, score in ranked[:top_k]]