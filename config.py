# rag_project/config.py


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "google/flan-t5-base"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

DB_PATH = "db/"
DATA_PATH = "data/raw/"
TOP_K = 5