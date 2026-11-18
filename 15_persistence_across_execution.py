from pathlib import Path
import chromadb

data_path = Path(__file__).resolve().parent / "data" / "persistence"

client = chromadb.PersistentClient(path=str(data_path))


collection = client.get_or_create_collection(
    name="persistent-practice",
    embedding_function=None
)

collection.upsert(
    ids=["saved-record"],
    embeddings=[[1.0,0.0,0.0]],
    documents=["The record survives a Python process restart."],
)

print("Storage:", data_path)
print("Record Count:", collection.count())
print(collection.get(ids=["saved-record"]))