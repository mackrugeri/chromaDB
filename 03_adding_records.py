from common import fresh_collection

_, collection = fresh_collection(seed=False)

collection.add(
    ids=["book-1","book-2"],
    embeddings=[
        [1.0,0.0,0.0],
        [0.0,1.0,0.0]
    ],
    documents=[
        "A beginner guide to Python.",
        "An Introduction to vector databases."
    ],
    metadatas=[
        {"topic": "python", "pages": 120},
        {"topic": "vector", "pages": 180}
    ]
)

print("Record Count:", collection.count())
print(collection.peek(limit=1)) # it retrieves and displays the first 2 records form a chromaDB collection