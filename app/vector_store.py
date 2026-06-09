import chromadb
from app.embedder import create_embeddings

client = chromadb.PersistentClient(
    path="./chroma_db"
)

def create_collection():

    return client.get_or_create_collection(
        name="collection"
    )

def store_chunks(
    collection,
    chunks,
    filename,
    page_num
):

    metadatas = [
        {
            "source": filename,
            "page_num": page_num,
            "chunk": i
        }
        for i in range(len(chunks))
    ]

    ids = [
        f"{filename}_page_{page_num}_id_{i}"
        for i in range(len(chunks))
    ]

    embeddings = create_embeddings(chunks)

    collection.add(
        documents=chunks, 
        ids=ids,
        metadatas=metadatas,
        embeddings=embeddings
    )

def retrieve(
    collection,
    question,
    n_results=20
):
    
    query_embedding = create_embeddings([question])

    return collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )