FROM python:3.12-slim

# 作業ディレクトリ
WORKDIR /app

# 必要パッケージ
RUN apt-get update && apt-get install -y build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 依存関係のコピーとインストール
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードのコピー
COPY app ./app

# ポート
EXPOSE 8000

# 起動コマンド
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
