from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session 


Base = declarative_base()

class CTF(Base):
    __tablename__ = 'ctfs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    link = Column(String)
    begin_date = Column(String)
    begin_time = Column(String)
    end_date = Column(String)
    end_time = Column(String)
    type = Column(String)
    place = Column(String)

def create_db():
    engine = create_engine('sqlite:///ctf.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
