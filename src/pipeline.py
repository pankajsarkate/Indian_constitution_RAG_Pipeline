
# from retrieval import get_retriever
# from generation import generate_answer
from config import TOP_K
from src.retrieval import get_vector_store
from src.generation import generate_answer

vector_store = get_vector_store()

def rag_pipeline(question):
    results = vector_store.similarity_search_with_score(question, k=TOP_K)

    scores = [score for _, score in results]
    min_score = min(scores)

    # dynamic filtering
    docs = [doc for doc, score in results if score <= min_score + 0.3]

    if not docs:
        return "I don't know."

    context = "\n\n".join([d.page_content for d in docs])

    # keyword sanity check
    if not any(word.lower() in context.lower() for word in question.split()):
        return "I don't know."

    return generate_answer(question, context)