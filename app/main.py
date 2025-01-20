import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

# .envファイルを読み込む
load_dotenv()

# 環境変数からAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")

# OpenAIクライアントの設定
llm = OpenAI(temperature=0.7, openai_api_key=api_key)

response = llm("LangChainとは何ですか？")
print(response)