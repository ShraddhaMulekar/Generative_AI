from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

app = FastAPI(
        title="Simple ChatBot API",
        description="An AI Chatbot API using LangGraph and FastAPI",
        version="1.0.0"
)

load_dotenv()


# Root Health Endpoint
@app.get("/")
def root():
        return {"message":"Simple AI Chatbot is running..."}

def initialize_chat():
        """
        Initializes the LangGraph-based chatbot with memory
        """

        try:
            llm = ChatOpenAI(model="gpt-5", temperature=0.8)

            class ChatBotState(TypedDict):
                   messages: Annotated[list, add_messages]

            graph = StateGraph(ChatBotState)

            def chat(state: ChatBotState) -> ChatBotState:
                   messages = state["messages"]
                   response = llm.invoke(messages)
                   return {"messages": [response]}

            graph.add_node("chat_node", chat)

            graph.add_edge(START,"chat_node")
            graph.add_edge("chat_node", END)

            conn = sqlite3.connect("memory.db", check_same_thread=False)

            memory = SqliteSaver(conn)

            workflow = graph.compile(checkpointer=memory)
            return workflow

        except Exception as e:
               print(f"Error initializing the chatbot: {e}")
               return None
        

chatbot = initialize_chat()

config = {
       "configurable": {
              "thread_id": "1"
       }
}

class ChatRequest(BaseModel):
       question: str

@app.post('/chat',tags=["Chatbot"])
def chat_endpoint(payload: ChatRequest):
       try:
              
              if not payload.question.strip():
                     return {"Error":"Question is require to get the chatbot started."}
              
              if chatbot is None:
                     return {"Error": "AI Service is not available at the moment. Please try again later."}
              
              result = chatbot.invoke({"messages":[HumanMessage(content=payload.question)]}, config=config)

              AIResponse = result["messages"][-1].content

              return {"response": AIResponse}
              
       except Exception as e:
              raise HTTPException(status_code=500, detail=f"Something went wrong. {e}")