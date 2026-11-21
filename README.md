# ChromaDB Workbook

A hands-on workbook for learning ChromaDB through Python examples, experiments, and practice exercises.

This repository focuses on vector database concepts and ChromaDB operations. Retrieval-Augmented Generation (RAG) is reserved for a separate project.

## Topics Covered

- In-memory, persistent, and HTTP clients
- Collection creation, inspection, modification, and deletion
- Adding documents, embeddings, and metadata
- Retrieving records and pagination
- Vector similarity search
- Metadata and document filtering
- Updating, upserting, and deleting records
- Cosine, squared L2, and inner-product distance
- Default and custom embedding functions
- Sentence Transformers integration
- Batch ingestion
- Persistent storage
- Logical export and import
- HNSW index configuration
- Synchronous and asynchronous server access
- Validation errors and troubleshooting
- Retrieval evaluation
- Optional Chroma Cloud examples

## Requirements

- Python 3.10 or newer
- ChromaDB `1.5.9`
- Internet access for package installation and embedding model downloads
- A Chroma Cloud account for optional Cloud examples

Core examples use handwritten embeddings and do not require an external embedding API.

## Installation

Clone this repository and open its directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Verify the installed version:

```bash
python -c "import chromadb; print(chromadb.__version__)"
```

For the Sentence Transformers lesson:

```bash
python -m pip install sentence-transformers
```

## Workbook Structure

```text
chromadb-workbook/
├── README.md
├── requirements.txt
├── common.py
├── 01_clients.py
├── 02_collections.py
├── 03_add_records.py
├── 04_get_records.py
├── 05_vector_search.py
├── 06_metadata_filters.py
├── 07_document_filters.py
├── 08_update_upsert.py
├── 09_delete_records.py
├── 10_distance_metrics.py
├── 11_default_embeddings.py
├── 12_sentence_transformers.py
├── 13_custom_embeddings.py
├── 14_batch_ingestion.py
├── 15_persistence.py
├── 16_export_import.py
├── 17_index_configuration.py
├── 18_server_client.py
├── 19_async_client.py
├── 20_validation_errors.py
├── 21_retrieval_evaluation.py
├── 22_cloud.py
├── PRACTICE.md
└── .gitignore
```

## Learning Path

| Stage | Lessons | Focus |
|---|---|---|
| Foundations | 01–04 | Clients, collections, records, and retrieval |
| Search and filtering | 05–07 | Nearest neighbors, metadata, and document filters |
| Data management | 08–09 | Updates, upserts, and deletion |
| Embeddings | 10–13 | Distance metrics and embedding functions |
| Storage and performance | 14–17 | Batching, persistence, export/import, and indexing |
| Deployment and debugging | 18–20 | HTTP clients, async operations, and errors |
| Evaluation and Cloud | 21–22 | Retrieval measurements and optional Cloud operations |

## Running the Examples

Run commands from the repository root so Python can import `common.py`.

```bash
python 01_clients.py
```

For example, to practice similarity search:

```bash
python 05_vector_search.py
```

Most core lessons create disposable, in-memory collections. The persistence lesson stores data under `data/`.

Some lessons have additional requirements:

| Lesson | Requirement |
|---|---|
| Default embeddings | Model download on first use |
| Sentence Transformers | Additional package and model download |
| Server and async clients | Running Chroma server |
| Cloud | Cloud credentials and an existing database |

## Running a Local Server

Start the server in one terminal:

```bash
chroma run --path ./data/server --host 127.0.0.1 --port 8000
```

Activate your virtual environment in another terminal, then run:

```bash
python 18_server_client.py
```

For the asynchronous example:

```bash
python 19_async_client.py
```

The server stores its data in `./data/server`. HTTP clients access that storage through the server.

## Optional Cloud Setup

Set the following environment variables before running the Cloud lesson:

- `CHROMA_API_KEY`
- `CHROMA_TENANT`
- `CHROMA_DATABASE`

**macOS / Linux**

```bash
export CHROMA_API_KEY="your-api-key"
export CHROMA_TENANT="your-tenant"
export CHROMA_DATABASE="your-database"

python 22_cloud.py
```

**Windows PowerShell**

```powershell
$env:CHROMA_API_KEY = "your-api-key"
$env:CHROMA_TENANT = "your-tenant"
$env:CHROMA_DATABASE = "your-database"

python 22_cloud.py
```

Keep credentials out of source files and Git commits. Cloud examples create resources; inspect and remove practice collections when finished.

## Important Concepts

### Collections and records

A collection contains records. These operations count different things:

```python
client.count_collections()  # Collections in the current database
collection.count()         # Records in one collection
```

### Retrieval versus similarity search

- `get()` retrieves records using IDs or filters.
- `query()` ranks eligible records by vector distance.
- `get()` returns flat record lists.
- `query()` returns nested lists, one per query.

### Filtering and ranking

Filters determine which records are eligible. The query embedding determines their similarity ranking.

If a filter matches two records and `n_results=2`, both may be returned for different queries. Compare distances as well as IDs.

### Embedding compatibility

All embeddings within a collection must have the same dimension. Stored vectors and query vectors must also use a compatible embedding model and preprocessing.

Matching dimensions alone do not make two models compatible.

### Distance scores

Smaller distances indicate closer matches under the selected metric. Distances are not confidence probabilities.

### Persistence

An ephemeral client does not preserve data across process restarts. A persistent client saves data to its configured directory.

## How to Practice

For each lesson:

1. Read the example and predict its output.
2. Run it and inspect the result.
3. Modify the data, query, or configuration.
4. Explain why the result changed.
5. Record your findings in `PRACTICE.md`.

Useful experiments include:

- Changing query vectors while keeping filters fixed
- Comparing `add()`, `update()`, and `upsert()`
- Reopening a collection in a new Python process
- Comparing distance metrics
- Measuring batch ingestion times
- Comparing approximate results with exact nearest neighbors
- Exporting records and verifying imported results

## Evaluation

The evaluation lesson compares approximate nearest neighbors against exact cosine rankings on synthetic vectors.

Record:

- Dataset size and embedding dimension
- Index configuration
- Recall at a chosen result count
- Query latency
- Hardware and software versions

Synthetic index recall measures nearest-neighbor accuracy. Evaluating semantic search also requires queries with human-labeled relevant documents.

## Troubleshooting

| Problem | What to check |
|---|---|
| Import failure | Confirm the virtual environment is active and dependencies are installed. |
| Dimension mismatch | Compare the dimensions of stored and query embeddings. |
| Unexpected collection count | Inspect existing collections and the persistent storage path. |
| Same search results | Inspect filters, eligible record count, distances, and ties. |
| Missing records after restarting | Confirm you used a persistent client and the same path. |
| Server connection failure | Confirm the server is running on the expected host and port. |
| Model download failure | Check network access and model cache permissions. |
| Validation error | Check list lengths, IDs, metadata types, and required inputs. |

## Further Study

- [ ] Loading documents from TXT, Markdown, and CSV files
- [ ] Stable IDs and duplicate handling
- [ ] Embedding model migration
- [ ] Multimodal search
- [ ] Tenant and database administration
- [ ] Backup and restore verification
- [ ] Docker deployment
- [ ] Deployment security
- [ ] Logging and monitoring
- [ ] Version upgrades and migrations
- [ ] Cloud sparse and hybrid search
- [ ] Automated integration checks

## References

- [Chroma documentation](https://docs.trychroma.com/)
- [Python client reference](https://docs.trychroma.com/reference/python/client)
- [Collection reference](https://docs.trychroma.com/reference/python/collection)
- [Metadata filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering)
- [Collection configuration](https://docs.trychroma.com/docs/collections/configure)
- [Chroma GitHub repository](https://github.com/chroma-core/chroma)