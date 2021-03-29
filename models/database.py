#DBとの直接的な接続の情報を格納
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'onegai.db')
# engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()

databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'qa_advance.db')
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)