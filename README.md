# Flask Audio Splitter（Flask音声分割器）
このシンプルなFlaskベースのWebアプリケーションは、ユーザーが音声ファイルをアップロードし、入力と出力のフォーマットを指定した後、1分間隔のチャンクとして音声ファイルをZIPファイルでダウンロードできます。

## 依存関係
- Python 3.x
- Flask
- pydub
- ffmpeg

## 実行方法
Dockerイメージをビルドします：

```
docker build -t flask-audio-splitter .
```
コンテナを実行します：
```
docker run -p 5000:5000 flask-audio-splitter
```

Webブラウザで http://localhost:5000 にアクセスします。

APIエンドポイント
/（GET、POST） - 音声をアップロードして1分間隔のチャンクとしてダウンロード。