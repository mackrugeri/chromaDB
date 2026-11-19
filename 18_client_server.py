# Terminal 1
# chroma run \
#   --path ./data/server \
#   --host 127.0.0.1 \
#   --port 8000

# Terminal 2: python 18_server_client.py
import chromadb

client = chromadb.HttpClient(
    host="127.0.0.1",
    port=8000,
)

print("Heartbeat:", client.heartbeat())

collection = client.get_or_create_collection(
    name="server-practice",
    embedding_function=None,
)

collection.upsert(
    ids=["http-record"],
    embeddings=[[1.0, 0.0]],
    documents=["Written through the HTTP client."],
)

print(collection.get(ids=["http-record"]))