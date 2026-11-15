# Squared L2 measures geometric separation. 
# Cosine distance compares vector direction. 
# Inner-product distance also depends on magnitude.

# L2 -> Eiuclidean Distance -> L2 measures the actual straight-line distance between two vectors.
# cosine distance -> cosine measures the difference in direction between two vectors.
# Inner Product -> measures how strongly two vectors align, including their magnitude.

# L2 asks: How far apart are these vectors?
# Cosine asks: Are these vectors pointing in the same direction?
# IP asks: How strongly do these vectors align, considering their magnitudes?

from math import sqrt
from uuid import uuid4

import chromadb

client = chromadb.EphemeralClient()

for metric in ["l2", "cosine", "ip"]:
    collection = client.create_collection(
        name =f"distance-{metric}-{uuid4().hex[:8]}",
        embedding_function=None,
        configuration={
            "hnsw": {"space": metric}
        }
    )

    collection.add(
        ids=["same", "longer", "opposite"],
        embeddings=[
            [1.0, 0.0],
            [2.0, 0.0],
            [-1.0, 0.0],
        ]
    )

    result = collection.query(
        query_embeddings=[[1.0, 0.0]],
        n_results=3,
        include=["distances"]
    )

    print(metric, list(zip(
        result["ids"][0],
        result["distances"][0]

    )))


#### Normalization 

### vector/ || vector ||

def normalization(vector):
    norm = sqrt(sum(value * value for value in vector))
    if norm == 0:
        raise ValueError("A zero vector has no direction")
    return [value / norm for value in vector]

print(f"Normalization of vector: {normalization([3.0,4.0])}")
