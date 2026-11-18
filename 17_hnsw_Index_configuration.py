from uuid import uuid4
import chromadb


client = chromadb.EphemeralClient()


collection = client.create_collection(
    name=f"configured-{uuid4().hex[:8]}",
    embedding_function=None,
    configuration={
        "hnsw": {
            "space": "cosine",
            "ef_construction": 200,
            "ef_search": 100,
            "max_neighbors": 32,
        }
    }
)

collection.add(
    ids=["a", "b", "c"],
    embeddings=[
        [1.0,0.0],
        [0.9, 0.1],
        [0.0, 1.0]
    ],
)

print(
    collection.query(
        query_embeddings=[[1.0,0.0]],
        n_results=2
    )
)