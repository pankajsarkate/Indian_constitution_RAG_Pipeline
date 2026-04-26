from transformers import pipeline
from config import *

generator = pipeline("text2text-generation", model=LLM_MODEL)

def generate_answer(question, context):
    prompt = f"""
        You are a strict question answering system.

        Rules:
        1. Answer ONLY using the context below
        2. If answer is NOT in the context → say "I don't know"
        3. DO NOT guess
        4. DO NOT make up answers

        Context:
        {context}

        Question: {question}

        Answer:
        """

    result = generator(prompt, max_length=200)
    return result[0]["generated_text"]