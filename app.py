
import streamlit as st
from src.pipeline import rag_pipeline

st.title("RAG Chatbot")

query = st.text_input("Ask something:")

if query:
    response = rag_pipeline(query)
    st.write(response)
