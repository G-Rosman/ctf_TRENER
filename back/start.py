from git_parser import all_ctf
from main import *
from fastapi import FastAPI
from database import create_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешить все домены, или укажите конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/today")
async def get_today_events():
    events = [{"id": record.id, "name": record.name, "link": record.link, "begin_date": record.begin_date, "end_date": record.end_date} for record in today]
    return JSONResponse(content=events)

@app.get("/tomorrow")
async def get_today_events():
    events = [{"id": record.id, "name": record.name, "link": record.link, "begin_date": record.begin_date, "end_date": record.end_date} for record in tomorrow]
    return JSONResponse(content=events)


