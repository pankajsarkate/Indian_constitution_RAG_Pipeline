
import os
from config import *
from transformers import pipeline
from config import *



# VERY IMPORTANT (must be before transformers import)
# os.environ["TRANSFORMERS_NO_TORCHVISION"] = "1"
# os.environ["TRANSFORMERS_NO_LIBROSA"] = "1"



# Load model
generator = pipeline(
    "text2text-generation",
    model=LLM_MODEL,
    device=-1  # CPU
)

def generate_answer(question, context):
    prompt = f"""
            You are a strict question answering system.

            Rules:
            1. Answer ONLY using the context
            2. If answer is not in context → say "I don't know"
            3. Do NOT guess

        Context:
        {context}

        Question: {question}

        Answer:
        """

    result = generator(prompt, max_length=200)
    return result[0]["generated_text"]