# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    # routes.py の init_app 関数をインポート
    from .routes import init_app
    init_app(app)

    return app
