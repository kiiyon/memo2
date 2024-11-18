# app.py
from app import create_app  # __init__.py で作成した create_app 関数をインポート

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # 開発用サーバーを起動
