from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from config import *

# Load model manually (no torchvision issue)
tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(LLM_MODEL)

def generate_answer(question, context):
    prompt = f"""
Answer only from the context.
If not found, say "I don't know".

Context:
{context}

Question: {question}
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=150)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)