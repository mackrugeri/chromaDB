from uuid import uuid4

import chromadb
client = chromadb.EphemeralClient()

name = f"lifecycle-{uuid4().hex[:12]}"

collection = client.create_collection(
    name=name,
    embedding_function=None, # You're choosing not to configure an automatic embedding function for the collection
    # which means that you must provide embeddings yourself when adding documents
    metadata={"purpose": "colletion lifecycle practice"}
)

same_collection = client.get_collection(
    name=name,
    embedding_function=None
)

print("Same collection:", collection.id == same_collection.id)
print("Name:", collection.name)
print("Metadata:", collection.metadata)

print("Collection", [
    item.name for item in client.list_collections()
])

print("Collection count:", client.count_collections())


new_name = f"{name}-renamed"

collection.modify(
    name= new_name,
    metadata={"purpose": "rename practice collection"}
)

print("Renamed:", client.get_collection(new_name).name)
client.delete_collection(name=new_name)