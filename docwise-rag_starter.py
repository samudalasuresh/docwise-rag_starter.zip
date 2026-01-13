import streamlit as st

st.set_page_config(page_title="DocWise — RAG Q&A", page_icon="📄")
st.title("📄 DocWise — RAG Document Q&A")
st.caption("Starter template. Add PDF upload → chunking → embeddings → retrieval → LLM answering.")

st.info("Next step: implement PDF ingestion + FAISS index + query retrieval.")
