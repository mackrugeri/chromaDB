from common import fresh_collection

client, collection = fresh_collection()

# deletion of python 
collection.delete(ids=["python"])
print(collection.get()["ids"])

# deletion with where condition

collection.delete(where={"published": False})
print(collection.get(where={"published": False})["ids"])

# deletion with where document condition

collection.delete(
    where_document={"$contains": "Pandas"}
)
print(collection.get()["ids"])

#deletion of complete collection
client.delete_collection(name=collection.name)

