from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import *


def get_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    return db