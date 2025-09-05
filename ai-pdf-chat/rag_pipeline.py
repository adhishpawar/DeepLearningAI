import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

class RAGPipeline:
    def __init__(self):
        self.vectorstore = None
        self.qa_chain = None

    def process_pdf(self, file_path: str):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)

        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
        self.vectorstore = FAISS.from_documents(chunks, embeddings)

        self.qa_chain = ConversationalRetrievalChain.from_llm(
            ChatOpenAI(openai_api_key=OPENAI_KEY),
            retriever=self.vectorstore.as_retriever()
        )

    def chat(self, query: str, chat_history=[]):
        if not self.qa_chain:
            return "No PDF uploaded yet."
        return self.qa_chain.run({"question": query, "chat_history": chat_history})

