# app/routes.py
from flask import render_template

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')  # index.htmlを表示

    @app.route('/<int:number>')
    def show_number(number):
        return render_template('index.html', number=number)  # URLで受け取ったnumberを表示

    @app.route('/about')
    def about():
        return render_template('about.html')  # about.htmlを表示

    @app.route('/hensu')
    def hensu():
        return render_template('hensu.html')  # hensu.htmlを表示
