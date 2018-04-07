from flask import Flask, render_template, request, redirect, url_for
# import logging

from migration import *

app = Flask(__name__)
# app.logger.setLevel(logging.WARNING)

@app.route('/')
def index():
    students = Student.__table__.select().execute().fetchall()
    return render_template('index.html', students=students)

@app.route('/break')
def hello():
    hoge = 'hogehoge'
    import pdb; pdb.set_trace()
    return 'hello'

@app.route('/create', methods=['POST'])
def create():
    return request.form['data'] + ' is posted !'

@app.route('/create_db')
def create_db():
    url        = 'mysql://root:password@localhost'
    new_engine = sql_al.create_engine(url, encoding='utf-8', echo=True)
    schema     = 'CREATE DATABASE IF NOT EXISTS `%s` DEFAULT CHARACTER SET utf8;' % 'flask_sample'
    result     = new_engine.connect().execute(schema)
    return 'DB is created !'

@app.route('/add_record')
def add_record():
    Student.__table__.insert().execute(name='お名前', kana='おなまえ')
    return redirect(url_for('index'))


if __name__ == '__main__':
    #app.config['DEBUG'] = True
    #app.debug = True
    #app.run()
    app.run(host='0.0.0.0', debug=True)
