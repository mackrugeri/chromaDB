from pathlib import Path
from common import fresh_collection
import json

_, source = fresh_collection()
_, destination = fresh_collection(seed=False)

export_path = Path("exports") / "records.json"
export_path.parent.mkdir(exist_ok=True)

records = []
page_size = 2

for offset in range(0, source.count(), page_size):
    page = source.get(
        limit=page_size,
        offset=offset,
        include=["documents","metadatas","metadatas"],
    )

    for index, record_id in enumerate(page["ids"]):
        records.append({
            "id": record_id,
            "document": page["documents"][index],
            "metadata": page["metadata"][index],
            "embedding":[
                float(value) for value in page["embeddings"][index]
            ]
        })

loaded = json.loads(export_path.read_text(encoding="utf-8"))

for record in loaded:
    payload ={
        "ids": [record["id"]],
        "embeddings": [record["embedding"]],
    }

    if record["document"] is not None:
        payload["documents"] = [record["document"]]
    if record["metadata"]:
        payload["metadatas"] = [record["metadata"]]


    destination.upsert(**payload)

assert destination.count() == source.count()
assert set(destination.get()["ids"]) == set(source.get()["ids"])


print("Exported and imported:", destination.count())