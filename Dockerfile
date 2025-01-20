# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステム依存パッケージをインストール
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 依存パッケージリストをコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 必要なアプリケーションコードのみをコピー
COPY app/ ./app

# 環境変数を設定 (任意)
ENV PYTHONUNBUFFERED=1

# デフォルトのコマンドを指定
CMD ["python3", "app/main.py"]
