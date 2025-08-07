from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS

dataset = load_dataset("open-r1/OpenR1-Math-220k", split="train")  

# 2. Prepareing texts and metadata
texts = [item["problem"] for item in dataset]
metadatas = [{"solution": item["solution"]} for item in dataset]

# 3. Loading embedding model and compute embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = embedding_model.encode(texts, show_progress_bar=True)

# 4. Building and saveing the FAISS vector database
vector_store = FAISS.from_embeddings(
    list(zip(texts, embeddings)),
    embedding_model,
    metadatas=metadatas
)
vector_store.save_local("database")  # Creating a folder with the FAISS index and metadata

print("FAISS vector database built and saved to: database/")
