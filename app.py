# 必要なモジュールをインポート
from flask import Flask, request, send_file, render_template
from pydub import AudioSegment
import os
import tempfile
import shutil

# Flaskアプリを初期化
app = Flask(__name__)

# ホームページのルートを定義
@app.route('/', methods=['GET', 'POST'])
def index():
    # POSTリクエストを処理
    if request.method == 'POST':
        # アップロードされた音声ファイルとフォーマットを取得
        file = request.files['audio']
        input_format = request.form.get('input_format')  
        output_format = request.form.get('output_format')  

        # 必要な情報がすべて揃っているか確認
        if file and input_format and output_format:
            # アップロードされたファイルを保存
            filepath = f"uploaded_audio.{input_format}"
            file.save(filepath)
            
            # 音声ファイルを読み込む
            audio = AudioSegment.from_file(filepath, format=input_format)
            
            # 一時ディレクトリを作成
            with tempfile.TemporaryDirectory() as tmpdirname:
                # チャンクの長さを定義（1分）
                chunk_length = 60 * 1000  
                # 音声をチャンクに分割
                chunks = [audio[i:i + chunk_length] for i in range(0, len(audio), chunk_length)]

                # 各チャンクを保存
                for i, chunk in enumerate(chunks):
                    chunk.export(f"{tmpdirname}/chunk_{i}.{output_format}", format=output_format)
                
                # チャンクをZIPファイルに圧縮
                shutil.make_archive('audio_chunks', 'zip', tmpdirname)

                # ZIPファイルをダウンロードできるように提供
                return send_file('audio_chunks.zip', as_attachment=True)

    # GETリクエストに対してHTMLテンプレートをレンダリング
    return render_template('index.html')

# アプリを実行
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
