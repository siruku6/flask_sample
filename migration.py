import sys
from db_conf import *

class Student(Base):
    __tablename__ = 'students'
    id   = sql_al.Column(sql_al.Integer, primary_key=True)
    name = sql_al.Column(sql_al.String(20)) # かっこ内の数字は文字列数の最大値
    kana = sql_al.Column(sql_al.String(40))

class StudentCols():
    get = Student.__table__.c
    # Student.__table__.delete().where(Student.__table__.c.id==1).execute()

# この処理でテーブル作成を実行
def main(args):
    Base.metadata.create_all()

if __name__ == "__main__":
    main(sys.argv)
