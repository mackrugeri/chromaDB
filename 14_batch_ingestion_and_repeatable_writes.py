from common import fresh_collection

# Batching controls request size. Upserts make rerunning a fixed dataset easier because stable IDs identify the same logical records.

client, collection = fresh_collection(seed=False)

total_records = 250
batch_size = min(50, client.get_max_batch_size())

for start in range(0, total_records, batch_size):
    stop = min(start + batch_size, total_records)
    print("*"*10)
    print(f"stop: {stop}")
    print("*"*10)
    numbers = list(range(start,stop))

    collection.upsert(
        ids=[f"item-{number}" for number in numbers],
        embeddings=[
            [float(number + 1), 1.0, 0.0]
            for number in numbers
        ],
        metadatas=[
            {"number": number}
            for number in numbers
        ]
    )

assert collection.count() == total_records
print("Inserted:", collection.count())