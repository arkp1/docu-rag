import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

def create_collection():

    try:
        client.delete_collection(
            "collection"
        )
    except:
        pass

    return client.get_or_create_collection(
        name="collection"
    )

def store_chunks(
    collection,
    chunks,
    filename
):

    metadatas = [
        {
            "source": filename,
            "chunk": i
        }
        for i in range(len(chunks))
    ]

    ids = [
        f"{filename}_id_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        documents=chunks,
        ids=ids,
        metadatas=metadatas
    )

def retrieve(
    collection,
    question,
    n_results=6
):

    return collection.query(
        query_texts=[question],
        n_results=n_results
    )