

import gradio as gr
from src.pipeline import rag_pipeline

def chat_fn(message, history):
    return rag_pipeline(message)

gr.ChatInterface(chat_fn).launch()