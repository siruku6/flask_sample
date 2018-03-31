import sqlalchemy as sql_al
import sqlalchemy.ext.declarative

url     = 'mysql://root:password@localhost/flask_sample'
SQL_Obj = sql_al.create_engine(url, echo=True)
Base    = sql_al.ext.declarative.declarative_base()
Base.metadata.bind = SQL_Obj
