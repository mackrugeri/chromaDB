from uuid import uuid4
import chromadb

from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2",
    normalize_embeddings=True
)

client = chromadb.EphemeralClient()

collection = client.create_collection(
    name=f"sentence-model-{uuid4().hex[:8]}",
    embedding_function=embedding_function,
    configuration={"hnsw": {"space": "cosine"}}
)

collection.add(
    ids=["transport", "food"],
    documents=[
        "Trains carry passengers between cities",
        "Oranges and apples are fruits"
    ]
)

print(
    collection.query(
        query_texts=["travel by railway"],
        n_results=1
    )
)