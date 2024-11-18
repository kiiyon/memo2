from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')  # templates フォルダの指定

    # アプリケーション設定
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # データベースの初期化
    db.init_app(app)

    # routes.py の import
    from .routes import init_app  # 相対インポート
    init_app(app)  # ここでinit_appを呼び出す

    return app