from langchain_community.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.agents import initialize_agent, AgentType
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_tavily import TavilySearch
import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning
from dotenv import load_dotenv
import os

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

# Loading environment
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")


# Loading LLM
llm1= ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=GOOGLE_API_KEY)
embedding_model = HuggingFaceEmbeddings(model_name ='all-MiniLM-L6-v2')

vector_store = FAISS.load_local("database", embedding_model, allow_dangerous_deserialization=True)


search_tool1 = TavilySearch()
@tool
def tavily_search(query:str):
    "Search the web as per the query"
    return search_tool1.run(query)



tools = [tavily_search,]
    
prompt1 = PromptTemplate(template="""You are a math tutor. Your goal is to answer math questions step by step.
                        Instructions:
                        - Use the tool called `search_tool` to search the web.
                        - If the search_tool gives a useful result, return that as the final answer immediately.
                        - Do not make up any information.
                        - Do not retry or overthink.
                        - If the search_tool doesn't help, return "answer not found".
                        QUESTION:{input}
                        Available tools:{tools}
                        Tool Names:{tool_names}"
                        {agent_scratchpad}""",
                        input_variables=["input", "agent_scratchpad", "tools", "tool_names"],)


prompt2 = PromptTemplate(template="""You are a math tutor. Your goal is to answer math questions step by step in a detailed manner.
                         Use easiest language possible so that user can undetstand.
                        Instructions:
                        - Use the tool called `search_tool` to search the web.
                        - If the search_tool gives a useful result, return that as the final answer immediately.
                        - Do not make up any information.
                        - Do not retry or overthink.
                        - If the search_tool doesn't help, return "answer not found".
                        QUESTION:{input}
                        Available tools:{tools}
                        Tool Names:{tool_names}"
                        {agent_scratchpad}""",
                        input_variables=["input", "agent_scratchpad", "tools", "tool_names"],)



def math_tutor_agent(query:str, feedback=False):
    if feedback:
        prompt = prompt1
    else:
        prompt = prompt2
    
    agent_executer = initialize_agent(tools=tools,
                                      llm=llm1,
                                      prompt = prompt,
                                      agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
                                      verbose=True,
                                      handle_parsing_errors=True)
    result = agent_executer.invoke({"input" : query})
    return result["output"]

