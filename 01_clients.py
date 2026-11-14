# An ephemeral client keeps data in memory. 
# A persistent client stores data on disk. 
# An HTTP client connects to a separately running Chroma server.

import chromadb

# Stores data temporarily in RAM.
memory_client = chromadb.EphemeralClient()

# Stores data permanently on local disk.
disk_client = chromadb.PersistentClient(
    path="./data/client_demo"
)


print("HeartBeat:", memory_client.heartbeat())
print("Backend version:", memory_client.get_version())

# Requires a running server
# server_client = chromadb.HttpClient(
#     host="127.0.0.1",
#     port=8000
# )

