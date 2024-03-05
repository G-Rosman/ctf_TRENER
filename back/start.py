from git_parser import all_ctf
from database import *
from PyQt5.QtWidgets import QApplication, QTextBrowser
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from gui import EventViewer
from main import find_events_next_day
from main import find_events
from fastapi import FastAPI
from database import create_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешить все домены, или укажите конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    app.state.db = create_db()
    all_ctf(app.state.db)

@app.get("/events")
async def get_today_events():
    find_events(app.state.db)
    find_events_next_day(app.state.db)


