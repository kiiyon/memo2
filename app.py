from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Flaskアプリケーションの初期化
app = Flask(__name__, template_folder='app/templates')  # template_folderの指定

# データベース設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# アプリケーションコンテキストを明示的に作成
def create_db():
    with app.app_context():
        db.create_all()  # 初回起動時にデータベースとテーブルを作成

# routes.py の import
from app.routes import init_app
init_app(app)  # ここでinit_appを呼び出す

if __name__ == '__main__':
    create_db()  # データベースを作成
    app.run(debug=True)