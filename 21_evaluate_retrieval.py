import random
import time
from math import sqrt
from uuid import uuid4

import chromadb

random_generator = random.Random(42)


def normalize(vector):
    norm = sqrt(sum(value * value for value in vector))
    return [value / norm for value in vector]


def cosine_distance(left, right):
    # Inputs are already normalized.
    return 1.0 - sum(a * b for a, b in zip(left, right))


dimension = 32
size = 500
k = 5

vectors = [
    normalize([
        random_generator.uniform(-1.0, 1.0)
        for _ in range(dimension)
    ])
    for _ in range(size)
]

ids = [f"vector-{index}" for index in range(size)]

client = chromadb.EphemeralClient()
collection = client.create_collection(
    name=f"evaluation-{uuid4().hex[:8]}",
    embedding_function=None,
    configuration={"hnsw": {"space": "cosine"}},
)

collection.add(ids=ids, embeddings=vectors)

recalls = []
latencies_ms = []

for _ in range(20):
    query = normalize([
        random_generator.uniform(-1.0, 1.0)
        for _ in range(dimension)
    ])

    exact_indices = sorted(
        range(size),
        key=lambda index: cosine_distance(query, vectors[index]),
    )[:k]

    expected = {ids[index] for index in exact_indices}

    started = time.perf_counter()
    result = collection.query(
        query_embeddings=[query],
        n_results=k,
        include=["distances"],
    )
    latencies_ms.append(
        (time.perf_counter() - started) * 1000
    )

    actual = set(result["ids"][0])
    recalls.append(len(actual & expected) / k)

print("Mean recall@5:", sum(recalls) / len(recalls))
print("Mean query ms:", sum(latencies_ms) / len(latencies_ms))