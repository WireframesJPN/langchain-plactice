import os
from dotenv import load_dotenv


from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from langchain_openai import ChatOpenAI

## IPythonで画像表示 (TODO: requirements.txtに追加する)
from IPython.display import Image, display

print("start....")

## Stateの定義
class State(TypedDict):
    messages: Annotated[list, add_messages]

## Graptの定義
graph_builder = StateGraph(State)

## Chat Nodeの準備
# 環境変数からAPIキーを取得
api_key = os.getenv("openai_api_key")
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", api_key=api_key)

## Nodeの定義
def chatbot(state: State):
  return { "messages": [llm.invoke(state["messages"])] }

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")

graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()


try:
   #display(Image(graph.get_graph().draw_mermaid_png()))
   print("print.....")
   print(graph.get_graph().draw_ascii())
except Exception:
  print(" Error: Graph is not available")
  # Exeptionの内容を表示
  print(e)
  pass


def stream_graph_updates(user_input: str):
  for event in graph.stream({ "messages": [ { "role": "user", "content": user_input } ] }):
    for value in event.values():
      print("Assistant:", value["messages"][-1].content)

while True:
  try:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
      print("Goodbye!")
      break
    stream_graph_updates(user_input)
  except:
    user_input = "What do you know about LangGraph?"
    print("User: " + user_input)
    stream_graph_updates(user_input)
    break
