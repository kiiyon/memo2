from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for  # requestを追加


# Flaskアプリケーションの初期化
app = Flask(__name__, template_folder='app/templates')  # template_folderの指定

# データベース設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# メモのデータベースモデル
class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# アプリケーションコンテキストを明示的に作成
def create_db():
    with app.app_context():
        db.create_all()  # 初回起動時にデータベースとテーブルを作成

# ホームページ（メモ一覧を表示）
@app.route('/')
def index():
    memos = Memo.query.all()  # すべてのメモを取得
    return render_template('index.html', memos=memos)

@app.route('/add', methods=['POST'])
def add():
    content = request.form.get('content')  # フォームからメモの内容を取得
    if content:
        new_memo = Memo(content=content)  # 新しいメモを作成
        db.session.add(new_memo)  # データベースに追加
        db.session.commit()  # コミットして保存
    return redirect(url_for('index'))  # メモ一覧ページにリダイレクト

if __name__ == '__main__':
    create_db()  # データベースを作成
    app.run(debug=True)