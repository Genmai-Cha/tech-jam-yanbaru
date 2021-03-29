# テーブルのカラム情報を定義するためのクラスを格納するためのファイル
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, event, engine
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship
from models.database import Base
from datetime import datetime


@event.listens_for(engine.Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.close()


class Question(Base):
    __tablename__ = 'questions'
    __table_args__ = (
        {'extend_existing': True},
    )
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(255))
    content = Column('content', Text)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    comments = relationship('Comment', backref='question', lazy=True)

    def __init__(self, title = None, content = None):
        self.title = title
        self.content = content
        now = datetime.now()
        self.created_at = now
        self.updated_at = now


class Comment(Base):
    __tablename__ = 'comments'
    __table_args__ = (
        {'extend_existing': True},
    )
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    question_id = Column(
      'question_id',
      Integer,
      ForeignKey('questions.id', onupdate='CASCADE', ondelete='CASCADE')
    )
    content = Column('content', Text)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __init__(self, question_id = None, content = None):
        self.question_id = question_id
        self.content = content
        now = datetime.now()
        self.created_at = now
        self.updated_at = now


class OnegaiContent(Base):
    __tablename__ = 'onegaicontents'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)