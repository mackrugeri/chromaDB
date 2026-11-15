from common import fresh_collection
_, collection = fresh_collection()

filters = {
    "equality": {"category": {"$eq": "database"}},
    "inequality": {"category": {"$ne": "database"}},
    "greater_than": {"year": {"$gt": 2024}},
    "greater_or_equal": {"year": {"$gte": 2024}},
    "less_than": {"year": {"$lt": 2025}},
    "less_or_equal": {"year": {"$lte": 2024}},
    "membership": {"category": {"$in": ["language", "analysis"]}},
    "not_membership": {"category": {"$nin": ["database"]}},
    "boolean": {"published": True},
    "and": {
        "$and": [
            {"category": "database"},
            {"year": {"$gte": 2024}},
        ]
    },
    "or": {
        "$or": [
            {"category": "language"},
            {"published": False},
        ]
    },
}


for label, condition in filters.items():
    print(label, collection.get(where=condition)["ids"])


result = collection.query(
    query_embeddings=[[0.0,0.0,0.0]],
    where={"category": "database"},
    n_results=2
)

print("Filtered nearest neighbors:", result["ids"])