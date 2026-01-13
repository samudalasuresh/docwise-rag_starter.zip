# DocWise — RAG Document Question Answering

DocWise is a Retrieval-Augmented Generation (RAG) system that allows users to
ask natural-language questions over their own documents and receive
accurate, context-grounded answers.

This project focuses on **LLM system design**, not just prompt usage.

---

## Why this project exists

Large Language Models can hallucinate when answering questions without
grounded context. In real-world applications (healthcare, legal, enterprise),
this is unacceptable.

DocWise solves this by combining:
- document retrieval
- vector search
- LLM reasoning

so answers are **based only on relevant source content**.

---

## What this project does

- Ingests PDF and text documents
- Chunks and embeds document content
- Stores embeddings in a vector database
- Retrieves the most relevant context per query
- Generates answers using an LLM constrained to retrieved context
- Returns answers with source grounding

---

## High-level architecture

1. **Document ingestion**
   - Upload PDFs or text files
   - Extract and clean text

2. **Chunking & embeddings**
   - Split documents into semantic chunks
   - Convert chunks into vector embeddings

3. **Vector search**
   - Store embeddings in FAISS
   - Retrieve top-k relevant chunks for a query

4. **LLM generation**
   - Pass retrieved context + question to LLM
   - Generate grounded answers

5. **User interface**
   - Simple Streamlit UI for uploads and chat

---

## Tech stack

- Python
- FAISS (vector similarity search)
- FastAPI (backend API)
- Streamlit (UI)
- OpenAI / local LLMs
- NumPy / PyPDF

---

## Why this matters in production

This architecture mirrors how real GenAI systems are built:
- Reduces hallucinations
- Improves factual accuracy
- Enables enterprise data usage
- Scales to large document collections

It is the foundation for:
- internal knowledge assistants
- legal/medical document QA
- enterprise search tools

---

## How to run locally

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
