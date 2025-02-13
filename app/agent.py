import os
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase
from langchain_openai import OpenAI

api_key = os.getenv("openai_api_key")
db = SQLDatabase.from_uri("sqlite:///data/test.db")
llm = OpenAI(temperature=0.2, openai_api_key=api_key)

db_chain = SQLDatabaseChain(database=db, llm=llm, verbose=True)
db_chain.run("野菜の合計金額はいくらですか？")