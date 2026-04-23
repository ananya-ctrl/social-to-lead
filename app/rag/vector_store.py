from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from app.config import GOOGLE_API_KEY


def create_vector_store(raw_text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_text(raw_text)
    documents = [Document(page_content=chunk) for chunk in chunks]

    embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY
)

    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store