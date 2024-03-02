from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session 
from datetime import datetime, timedelta


current_datetime = datetime.utcnow()
formatted_date = current_datetime.strftime("%d %b.")
formatted_time = current_datetime.strftime("%H:%M UTC")

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




def print_ctf_values(session: Session):
    ctf_records = session.query(CTF).all()
    print("ID | Name | Description | Begin Date | End Date")
    print("---|------|-------------|------------|---------")
    for record in ctf_records:
        print(f"{record.id} | {record.name}  | {record.begin_date} | {record.end_date}")

def find_events(session: Session):
    ctf_records = session.query(CTF).filter(CTF.begin_date == formatted_date).all()
    return ctf_records

def find_events_next_day(session: Session):
    next_day = (datetime.utcnow() + timedelta(days=1)).strftime("%d %b.")
    ctf_records = session.query(CTF).filter(CTF.begin_date == next_day).all()
    return ctf_records

