from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=GOOGLE_API_KEY)
def is_math_query(query:str):
    prompt = PromptTemplate(template="""Chek if the given query is a math query or not. Answer ONLY in Yes or No. 
                            - If a user asks anything in the feild of mathematics,statistics, algebra, calculus  ,mensuration, number systems etc. then that query would be regarded as a math query.
                        query:{query}""")
    prompt1 = prompt.format(query=query)
    result = llm.invoke(prompt1)
    return "yes" in result.content.lower()
    