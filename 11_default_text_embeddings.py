"""
    An embedding function turns text into vectors. 
    Use the same embedding model for stored documents and incoming queries.
"""

from uuid import uuid4

import chromadb
from chromadb.utils.embedding_functions import (
    DefaultEmbeddingFunction
)

embedding_function = DefaultEmbeddingFunction()


sample_vectors = embedding_function([
    "A cat is sleeping",
    "A database stores records"
])

# print("Sample Vector result:", sample_vectors)
print("Embedding Dimension:", len(sample_vectors[0]))   

client = chromadb.EphemeralClient()

collection = client.create_collection(
    name=f"text-{uuid4().hex[:8]}",
    embedding_function=embedding_function,
    configuration={"hnsw": {"space": "cosine"}}
)


collection.add(
    ids=["animals", "storage", "cooking"],
    documents=[
        "Cats and dogs are common household pets.",
        "Database store and retrieve information.",
        "Bread is baked using flour and yeast."
    ]
)
result = collection.query(
    query_texts=["Where can information be saved?"],
    n_results=1,
    include=["documents","distances"]
)

print(result)
