from sqlalchemy import text
from sqlalchemy import create_engine
import pandas as pd

df = pd.DataFrame({
  "name": ["リンゴ", "オレンジ", "バナナ", "玉ねぎ", "じゃがいも"],
  "price": [100, 150, 200, 50, 80],
  "category": ["フルーツ", "フルーツ", "フルーツ", "野菜", "野菜"]
})

sql_uri = "sqlite:///data/test.db"
engine = create_engine(sql_uri)
df.to_sql("products", con=engine, if_exists="replace")


with engine.connect() as conn:
  print(conn.execute(text("SELECT * FROM products")).fetchall())