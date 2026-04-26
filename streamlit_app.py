
import streamlit as st
from src.pipeline import rag_pipeline

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("📚 RAG Chatbot - Ask About Your Documents")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Ask a question...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate answer
    response = rag_pipeline(user_input)

    # Show assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

        