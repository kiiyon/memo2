from flask import render_template, request, redirect, url_for  # url_forをインポート
from . import db  # dbをインポート
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
    
    @app.route('/edit/<int:memo_id>', methods=['GET', 'POST'])
    def edit(memo_id):
        memo = Memo.query.get_or_404(memo_id)  # 該当するメモを取得
        if request.method == 'POST':
            new_content = request.form.get('content')  # 新しい内容を取得
            if new_content:
                memo.content = new_content  # メモを更新
                db.session.commit()  # 保存
            return redirect(url_for('index'))  # メモ一覧ページにリダイレクト
        return render_template('edit.html', memo=memo)  # 編集フォームを表示

    @app.route('/delete/<int:memo_id>', methods=['POST'])
    def delete(memo_id):
        memo = Memo.query.get_or_404(memo_id)  # メモを取得
        db.session.delete(memo)  # メモを削除
        db.session.commit()  # 保存
        return redirect(url_for('index'))  # メモ一覧ページにリダイレクト