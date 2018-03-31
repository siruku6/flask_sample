from flask import Flask, render_template, request
# import logging

from migration import *

app = Flask(__name__)
# app.logger.setLevel(logging.WARNING)

@app.route('/')
def index():
    return render_template('index.html')

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
    schema = 'CREATE DATABASE IF NOT EXISTS `%s`;' % 'sample_tmp_db'
    result = SQL_Obj.connect().execute(schema)
    return 'DB is created ? ' + str(result)

@app.route('/add_record')
def add_record():
    Student.__table__.drop(SQL_Obj)
    return 'テーブルを作成しました！'


if __name__ == '__main__':
    #app.config['DEBUG'] = True
    #app.debug = True
    #app.run()
    app.run(host='0.0.0.0', debug=True)
