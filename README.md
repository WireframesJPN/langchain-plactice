# とりあえず LangChain 練習環境

## 起動方法

### .env を作成

```
OPENAI_API_KEY={GPTのAPIキー}
```

### docker 起動

ディレクトリに移動して以下を実行

```sh
$ docker compose up -d
```

## コマンドの実行（いまのところ）

```sh
$ docker compose exec langchain_app bash
$ cd app
$ python main.py
```
