# memory.py
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.documents import Document

embeddings = OllamaEmbeddings(model="llama3")

def save_to_memory(insight: str, vectorstore_path="faiss_store"):
    doc = Document(page_content=insight)
    try:
        db = FAISS.load_local(vectorstore_path, embeddings,
                   allow_dangerous_deserialization=True)
        db.add_documents([doc])
    except:
        db = FAISS.from_documents([doc], embeddings)
    db.save_local(vectorstore_path)

def retrieve_similar(query: str, vectorstore_path="faiss_store"):
    try:
        db = FAISS.load_local(vectorstore_path, embeddings,
                   allow_dangerous_deserialization=True)
        results = db.similarity_search(query, k=2)
        return [r.page_content for r in results]
    except:
        return []