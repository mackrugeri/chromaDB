import asyncio

import chromadb


async def main():
    client = await chromadb.AsyncHttpClient(
        host="127.0.0.1",
        port=8000,
    )

    print(await client.heartbeat())

    collection = await client.get_or_create_collection(
        name="async-practice",
        embedding_function=None,
    )

    await collection.upsert(
        ids=["async-record"],
        embeddings=[[1.0, 0.0]],
    )

    print(await collection.count())

    result = await collection.query(
        query_embeddings=[[1.0, 0.0]],
        n_results=1,
    )

    print(result["ids"])


if __name__ == "__main__":
    asyncio.run(main())

# Inside a notebook, call:
# await main()