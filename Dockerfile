# オフィシャルなPythonランタイムを親イメージとして使用
FROM python:3.9-slim

# 音声処理のためのffmpegをインストール
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# コンテナ内での作業ディレクトリを設定
WORKDIR /app

# 現在のディレクトリの内容をコンテナの/appにコピー
COPY . /app

# requirements.txtで指定された必要なパッケージをインストール
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# ポート5000を外部に公開
EXPOSE 5000

# コンテナが起動するとapp.pyを実行
CMD ["python", "app.py"]
