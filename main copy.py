from git_parser import all_ctf
from database import *
from PyQt5.QtWidgets import QApplication, QTextBrowser
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from gui import EventViewer


session = create_db()
all_ctf(session)
today = find_events(session)
tomorrow = find_events_next_day(session)

if __name__ == "__main__":
    app = QApplication([])
    records = today + tomorrow
    viewer = EventViewer(records)
    viewer.show()
    app.exec_()
