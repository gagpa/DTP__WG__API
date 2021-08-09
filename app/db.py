from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from configs import db

Base = declarative_base()

engine = create_engine(db.URL, echo=False)
connection = engine.connect()
SessionFactory = sessionmaker(bind=engine, autoflush=False)
Session = scoped_session(SessionFactory)
