from common import fresh_collection
_,collection = fresh_collection()

get_result = collection.get( where_document={"$contains": "Python"} )["ids"]
print(get_result)

get_result = collection.get( where_document={"$not_contains": "Python"})["ids"]
print(get_result)


get_result = collection.get(
    where_document={
        "$or": [
            {"$contains": "Python"},
            {"$contains": "database"},
        ]
    }
)["ids"]


print(get_result)


result = collection.query(
    query_embeddings=[[1.0,0.0,0.0]],
    where={"published": True},
    where_document={"$contains": "Python"},
    n_results=2
)

print(result["ids"])