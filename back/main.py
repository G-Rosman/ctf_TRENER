from git_parser import all_ctf, init
from database import CTF, create_db
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

current_datetime = datetime.utcnow()
formatted_date = current_datetime.strftime("%d %b")
formatted_time = current_datetime.strftime("%H:%M UTC")

init()
session = create_db()
all_ctf(session)

def print_ctf_values(session: Session):
    # Запрос всех записей CTF из базы данных
    ctf_records = session.query(CTF).all()

    # Вывод заголовка таблицы
    print("ID | Name | Link | Begin Date | End Date")
    print("---|------|------|------------|---------")

    # Вывод каждой записи CTF
    for record in ctf_records:
        print(f"{record.id} | {record.name} | {record.link} | {record.begin_date} | {record.end_date}")

def find_events(session: Session):
    ctf_records = session.query(CTF).filter(CTF.begin_date == formatted_date).all()

    return ctf_records

def find_events_next_day(session: Session):
    next_day = (datetime.utcnow() + timedelta(days=2)).strftime("%d %b")
    print(next_day)
    ctf_records = session.query(CTF).filter(CTF.begin_date == next_day).all()
    return ctf_records


today = find_events(session)
tomorrow = find_events_next_day(session)