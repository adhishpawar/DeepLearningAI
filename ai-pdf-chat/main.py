from fastapi import FastAPI, UploadFile, Form
from rag_pipeline import RAGPipeline
import shutil

app = FastAPI()
rag = RAGPipeline()
chat_history = []

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    rag.process_pdf(file_path)
    return {"message": "PDF uploaded and processed"}

@app.post("/chat/")
async def chat(query: str = Form(...)):
    answer = rag.chat(query, chat_history)
    chat_history.append((query, answer))
    return {"answer": answer}
