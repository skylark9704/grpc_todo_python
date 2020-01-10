from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('mysql://root:root@localhost/todo', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
