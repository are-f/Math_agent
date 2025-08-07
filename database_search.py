from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from agent import math_tutor_agent  
import os

# Loading embeddings and vectorstore
embedding_model = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
vector_store = FAISS.load_local("database", embedding_model, allow_dangerous_deserialization=True)

def check_vectorstore(query: str, threshold: float = 0.75) -> str:
    """
    Checks FAISS vector store for relevant answer.
    If found, returns step-by-step solution from metadata.
    """
    docs = vector_store.similarity_search_with_score(query, k=1)

    if not docs:
        return None

    content, score = docs[0]
    if score > threshold:
        return None  # Not relevant enough

    problem = content.page_content
    solution = content.metadata.get("solution", "No solution available.")

    return f"Problem (from DB): {problem}\n\nStep-by-step Solution:\n{solution}"

def run_math_tutor(query: str, feedback = False):
    print(f"\nQuery: {query}")

    # Step 1: Checking vector store 
    answer = check_vectorstore(query)

    if answer:
        print("\nAnswer from Vector Store:\n")
        print(answer)
    else:
        # Step 2: Calling to agent (uses web search)
        print("\nNo match found in vector store. Using web search...\n")
        result = math_tutor_agent(query,feedback)
        print("\nAnswer from Agent (Web Search):\n")
        return result

