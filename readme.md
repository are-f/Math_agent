# 🧠 Math Tutor AI Agent

A smart math tutor agent built using LangChain, Gemini , and Hugging Face embeddings. It uses RAG, web search, and human feedback to answer math-related questions step-by-step.

---

## 🚀 Features

-  **LLM-Powered Tutoring** — Gemini 2.0 generates clear math solutions.
-  **Semantic Search** — Local vector DB with FAISS + Hugging Face embeddings.
-  **Web Search Tool** — Integrates DuckDuckGo or Tavily for real-time answers.
- **Feedback Learning** — Collects feedback to improve future answers.
- **Modular Codebase** — Clean structure for easy maintenance and extension.

---

## 🗂️ Project Structure

math_agent

├── agent.py

├── knowledge_base.py 

├── guardrails.py

├── main.py 

├── database── index.faiss---index.pkl (These are created automatically when you run knowledge_base.py)

└── requirements.txt


# How to run:
1. Step1: Run knowledge_base.py to load the dataset and FAISS vector store
2. Step2: Run main.py and give your query


# Sample Queries:

From DB:
1. What is the derivative of sin(x)?
2. Solve the equation: 2x + 3 = 7
3. What is the integral of x^2?
4. Find the area of a circle with radius r.
5. What is the limit of (1 + 1/n)^n as n approaches infinity?

Web search:

6. How do you compute the derivative of a function involving both sine and cosine?
7. How many faces does a truncated icosahedron have?
8. Explain the binomial theorem with real-life examples.
9. What is the standard deviation formula in statistics?
10. What is the Riemann hypothesis?

Ans not found:

11. Tell me about the triangle of infinity and zero.
12. Solve the paradox of rotating prime cube roots.
13. Explain the equation of everything in imaginary space.
14. What is the mathematical proof for God?
15. Why is 7 heavier than 3 in calculus?






