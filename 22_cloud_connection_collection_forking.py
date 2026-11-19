import os
from uuid import uuid4

import chromadb

client = chromadb.CloudClient(
    api_key=os.environ["CHROMA_API_KEY"],
    tenant=os.environ["CHROMA_TENANT"],
    database=os.environ["CHROMA_DATABASE"],
)

name = f"cloud-workbook-{uuid4().hex[:8]}"

collection = client.create_collection(
    name=name,
    embedding_function=None,
)

collection.add(
    ids=["original"],
    embeddings=[[1.0, 0.0]],
)

fork = collection.fork(new_name=f"{name}-fork")

fork.upsert(
    ids=["experiment"],
    embeddings=[[0.0, 1.0]],
)

print("Original count:", collection.count())
print("Fork count:", fork.count())

# Optional cleanup after inspection:
# client.delete_collection(name=fork.name)
# client.delete_collection(name=collection.name)