import chromadb

client = chromadb.Client(
    settings=chromadb.Settings(persist_directory="chroma_db")
)

collection = client.get_or_create_collection(name="rag_docs")

def store_chunks(chunks, embeddings):
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(
        documents=[chunk],
        embeddings=[emb],
        ids=[f"doc_{i}"]
        )

def search(embedding, k=5):
    return collection.query(
    query_embeddings=[embedding],
    n_results=k
    )