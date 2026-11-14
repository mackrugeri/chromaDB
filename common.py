from uuid import uuid4

import chromadb


IDS = ["python", "chroma", "postgres", "pandas"]

DOCUMENTS = [
    "Python is a general-purpose programming language.",
    "Chroma stores embeddings for vector similarity search.",
    "PostgreSQL is a relational database with SQL support.",
    "Pandas provides tools for data analysis in Python.",
]

METADATAS = [
    {"category": "language", "year": 2024, "published": True},
    {"category": "database", "year": 2025, "published": True},
    {"category": "database", "year": 2023, "published": False},
    {"category": "analysis", "year": 2025, "published": True},
]

# Illustrative axes: programming, vector search, relational storage.
EMBEDDINGS = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.8, 0.2, 0.0],
]


def fresh_collection(seed=True):
    client = chromadb.EphemeralClient()

    collection = client.create_collection(
        name=f"practice-{uuid4().hex[:12]}",
        embedding_function=None,
        configuration={
            "hnsw" : { # hnsw -> Hierarchical Navigable Small World
                "space": "cosine" # cosine -> Compares Vector direction
            }
        }
        # other namespaces
        # l2 -> Euclidean Distance
        # ip -> Inner product distance
    )

    if seed:
        collection.add(
            ids=IDS,
            embeddings=EMBEDDINGS,
            documents=DOCUMENTS,
            metadatas=METADATAS
        )
    return client, collection