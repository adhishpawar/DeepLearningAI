# 📄 AI-powered PDF Reader with Chat (FastAPI + LangChain)

This project is an **AI-powered PDF reader** where users can upload PDFs and **interactively chat** with their content.  
It uses **LangChain**, **OpenAI LLMs**, and **FastAPI** to build a **Retrieval-Augmented Generation (RAG)** pipeline.  
The goal is to provide an industry-level learning project that demonstrates semantic search, context-aware answers, and conversational AI.

---

## 🚀 Features
- Upload a PDF and extract text
- Chunk documents and generate embeddings
- Store embeddings in **FAISS** (local vector database)
- Ask natural language questions about the PDF
- Semantic search + LLM to generate accurate answers
- Maintains **chat history** for contextual responses
- REST API built using **FastAPI**
- Optional **Streamlit UI** for interaction

---

## 🛠️ Tech Stack
- **Backend:** FastAPI
- **LLM Orchestration:** LangChain
- **Embeddings & Chat Models:** OpenAI (`text-embedding-3-small`, GPT-3.5/4)
- **Vector DB:** FAISS
- **PDF Processing:** LangChain’s PyPDFLoader
- **Frontend (optional):** Streamlit or React

---

## 📂 Project Structure
ai_pdf_chat/
│── main.py # FastAPI entrypoint
│── rag_pipeline.py # LangChain RAG pipeline
│── models.py # Pydantic request/response schemas
│── database.py # VectorDB/SQLite handling (optional)
│── streamlit_app.py # Optional frontend UI
│── requirements.txt # Dependencies
│── .env # API Keys

---
