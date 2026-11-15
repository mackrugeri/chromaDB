from common import fresh_collection

_, collection = fresh_collection()

collection.update(
    ids=["python"],
    documents=["Python supports scripting and data analysis."],
    embeddings=[[0.95,0.05,0.0]]
)

# Read and Merge metadata to explicity preserve existing fields
existing_meta_data = collection.get(
    ids=["python"],
    include=["metadatas"]
)["metadatas"][0]

collection.update(
    ids=["python"],
    metadatas=[{**existing_meta_data, "reviewed": True}]
)

count_before_upsert = collection.count()

collection.upsert(
    ids=["python", "numpy"],
    documents=[
        "Python is used for scientific programming.",
        "NumPy supports numerical array operations."
    ],
    embeddings=[
        [0.95, 0.05, 0.0],
        [0.85, 0.15, 0.0]
    ],
)

assert collection.count() == count_before_upsert + 1

print(collection.get(ids=["python", "numpy"]))