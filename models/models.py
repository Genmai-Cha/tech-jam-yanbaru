# テーブルのカラム情報を定義するためのクラスを格納するためのファイル
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, event, engine
from models.database import Base
from datetime import datetime


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True,autoincrement = True)
    title = Column(String(128), unique=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

    def __init__(self, title=None, content=None, created_at=None,updated_at=None):
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at
    def __repr__(self):
        return '<Title %r>' % (self.title)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True,autoincrement = True)
    question_id = Column( 'question_id',Integer,ForeignKey('questions.id', onupdate='CASCADE', ondelete='CASCADE'))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime,default=datetime.now(), nullable=False)

    def __init__(self, question_id=None, content=None, created_at=None,updated_at=None):
        self.question_id = question_id
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at


