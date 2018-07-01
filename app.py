from flask    import Flask, render_template, request, redirect, url_for
from werkzeug import ImmutableDict
# import logging
from flask_bootstrap import Bootstrap
from sqlsoup         import SQLSoup
db = SQLSoup('mysql://root:password@localhost/flask_sample?charset=utf8')

class FlaskWithHamlish(Flask):
    jinja_options = ImmutableDict(
        extensions=['jinja2.ext.autoescape',
                    'jinja2.ext.with_',
                    'hamlish_jinja.HamlishExtension'])

# app = Flask(__name__)
app = FlaskWithHamlish(__name__)
app.jinja_env.hamlish_mode = 'indented'
app.jinja_env.hamlish_enable_div_shortcut = True
bootstrap = Bootstrap(app)

# app.logger.setLevel(logging.WARNING)

@app.route('/')
def index():
    # students = Student.__table__.select().execute().fetchall()
    students = db.students.all()
    return render_template('index.haml', students=students)

@app.route('/', methods=['POST'])
def create():
    name = request.form['name']
    # Student.__table__.insert().execute(name=name, kana='おなまえ')
    db.students.insert(name=name, kana='おなまえ')
    db.commit()
    return redirect(url_for('index'))

@app.route('/<int:id>')
def edit(id):
    # student = Student.__table__.select().where(StudentCols.get.id==id).execute().fetchall()
    student = db.students.filter(db.students.id==id).one()
    db.commit()
    # import pdb; pdb.set_trace()
    return render_template('edit.haml', student=student)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    # Student.__table__.update().where(StudentCols.get.id==id).execute(
    #     id   = request.form['id'],
    #     name = request.form['name'],
    #     kana = request.form['kana']
    # )
    db.students.filter_by(id=id).update({
        'id':   request.form['id'],
        'name': request.form['name'],
        'kana': request.form['kana']
    })
    db.commit()
    return redirect(url_for('index'))

@app.route('/<int:id>', methods=['POST'])
def destroy(id):
    # Student.__table__.delete().where(StudentCols.get.id==id).execute()
    # db.students.filter_by(id=id).delete()
    db.delete(db.students.filter_by(id=id).one())
    db.commit()
    return redirect(url_for('index'))

@app.route('/break')
def hello():
    hoge = 'hogehoge'
    import pdb; pdb.set_trace()
    return render_template('hamlish.haml', test='hello')

@app.route('/post_test', methods=['POST'])
def create_test():
    return request.form['data'] + ' is posted !'

@app.route('/create_db')
def create_db():
    import sqlalchemy as sql_al
    url        = 'mysql://root:password@localhost'
    new_engine = sql_al.create_engine(url, encoding='utf-8', echo=True)
    schema     = 'CREATE DATABASE IF NOT EXISTS `%s` DEFAULT CHARACTER SET utf8;' % 'flask_sample'
    result     = new_engine.connect().execute(schema)
    return 'DB is created !'

if __name__ == '__main__':
    #app.config['DEBUG'] = True
    #app.debug = True
    #app.run()
    app.run(host='0.0.0.0', debug=True)
