from common import fresh_collection

_, collection = fresh_collection()


def demonstrate(label, operation):
    try:
        operation()
    except Exception as error:
        # Broad handling is intentional for this error demonstration.
        print(label)
        print(type(error).__name__, str(error))


demonstrate(
    "Wrong query dimension",
    lambda: collection.query(
        query_embeddings=[[1.0, 0.0]],
        n_results=1,
    ),
)

demonstrate(
    "Different list lengths",
    lambda: collection.add(
        ids=["new-a", "new-b"],
        embeddings=[[1.0, 0.0, 0.0]],
    ),
)

demonstrate(
    "Duplicate IDs inside one request",
    lambda: collection.add(
        ids=["duplicate", "duplicate"],
        embeddings=[
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
    ),
)

demonstrate(
    "Documents without an embedding function",
    lambda: collection.add(
        ids=["missing-vector"],
        documents=["No function exists to embed this text."],
    ),
)

# Missing IDs in get() are not necessarily errors.
print(collection.get(ids=["does-not-exist"])["ids"])