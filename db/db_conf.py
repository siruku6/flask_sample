import sqlalchemy as sql_al
import sqlalchemy.ext.declarative

# https://qiita.com/ru_pe129/items/de7878b7043612aa86e1
url     = 'mysql://root:password@localhost/flask_sample?charset=utf8'
SQL_Obj = sql_al.create_engine(url, encoding='utf-8', echo=True)
Base    = sql_al.ext.declarative.declarative_base()
Base.metadata.bind = SQL_Obj
