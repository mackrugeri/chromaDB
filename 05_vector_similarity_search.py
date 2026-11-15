from common import fresh_collection

_, collection = fresh_collection()

result = collection.query(
    query_embeddings=[
        [0.0,1.0,0.0], # Near the Chroma record.
        [1.0,0.0,0.0], # Near the Python record.
    ],
    n_results=2,
    include=["documents","metadatas","distances"]
)

print(f"result: {result}")