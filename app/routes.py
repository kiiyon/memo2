from flask import render_template
from . import db
from .models import Memo

def init_app(app):
    @app.route('/')
    def index():
        memos = Memo.query.all()  # すべてのメモを取得
        return render_template('index.html', memos=memos)

    @app.route('/about')
    def about():
        return render_template('about.html')  # about.htmlを表示

    @app.route('/hensu')
    def hensu():
        return render_template('hensu.html')  # hensu.htmlを表示
    
    @app.route('/add', methods=['POST'])
    def add():
        content = request.form.get('content')  # フォームからメモの内容を取得
        if content:
            new_memo = Memo(content=content)  # 新しいメモを作成
            db.session.add(new_memo)  # データベースに追加
            db.session.commit()  # コミットして保存
        return redirect(url_for('index'))  # メモ一覧ページにリダイレクト
