# 1. ベースイメージとして軽量なPythonイメージを使用
FROM python:3.10-slim

# 2. 作業ディレクトリを /app に設定
WORKDIR /app

# 3. 依存ファイルを先にコピーしてキャッシュを活用
COPY requirements.txt ./

# 4. 依存パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# 5. アプリケーションコードを全てコピー
COPY . .

# 6. コンテナ起動時に実行するコマンドを指定
CMD ["python", "app.py"]