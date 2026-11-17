from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
from uuid import uuid4
import chromadb


class keywordEmbeddingFunction(EmbeddingFunction[Documents]):

    def __init__(self):
        pass

    def __call__(self, input: Documents) -> Embeddings:
        vectors = []

        for text in input:
            text = text.lower()

            vectors.append([
                float(text.count("python")),
                float(text.count("database")),
                1.0,
            ])

        return vectors

    @staticmethod
    def name() -> str:
        return "workbook-keyword-embedding"

    def get_config(self) -> dict:
        return {}

    @staticmethod
    def build_from_config(config: dict):
        return keywordEmbeddingFunction()


client = chromadb.EphemeralClient()
collection = client.create_collection(
    name=f"custom-embedding-{uuid4().hex[:8]}",
    embedding_function=keywordEmbeddingFunction()
)

collection.add(
    ids=["a", "b"],
    documents=[
        "Python Python programming",
        "database database storage",
    ]
)

result = collection.query( 
    query_texts=["Python"], 
    n_results=1,
    include=["embeddings", "documents", "distances", "metadatas"]
)

print(result)