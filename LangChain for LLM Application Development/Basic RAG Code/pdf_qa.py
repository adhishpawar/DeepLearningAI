import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma

from langchain.chains import RetrievalQA

# Load API key from .env
load_dotenv()

# 1. Load the document
file_path = r"E:\02 Projects\13 DeepLearning\LangChain for LLM Application Development\Basic RAG Code\demo.txt"

if os.path.exists(file_path):
    print("✅ File exists. Loading...")
    loader = TextLoader(file_path, encoding='utf-8')  
    docs = loader.load()
else:
    print("❌ File not found:", file_path)
    exit()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 3. Create embeddings using OpenAI
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# 4. Create Chroma vector store (in-memory)
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="rag-chroma"
)

# 5. Create Retriever
retriever = vectorstore.as_retriever()

# 6. Load the LLM
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0)

# 7. Create QA chain (RAG pipeline)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# 8. Ask a question!
question = "What is the main Topic?"
result = qa_chain.invoke({"query": question})

# 9. Print result
print("🔹 Question:", question)
print("✅ Answer:", result['result'])
