from common import fresh_collection

_, collection = fresh_collection()

records = collection.get(
    ids=["python","pandas"],
    include=["documents", "metadatas", "embeddings"]
)

# enumerate() adds an index (counter) to each item in an iterable

for index, record_id in enumerate(records["ids"]):
    print(record_id)
    print(records["documents"][index])
    print(records["metadatas"][index])
    print(records["embeddings"][index])

print("Preview:", collection.peek(limit=2))
print("Preview all:", collection.peek())

page_size = 2

for offset in range(0, collection.count(), page_size):
    page = collection.get(
        limit=page_size,
        offset=offset,
        include=["documents"],
    )
    print("Page:", page["ids"])