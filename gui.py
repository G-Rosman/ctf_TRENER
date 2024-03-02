from PyQt5.QtWidgets import QTextBrowser
import os
class EventViewer(QTextBrowser):
    def __init__(self, records, parent=None):
        super(EventViewer, self).__init__(parent)
        self.setReadOnly(True)
        self.setOpenExternalLinks(True)
        self.setHtmlContent(records)



    def setHtmlContent(self, records):
        html_content = f"""
        <div style="width: calc(100% - 60px); padding: 5px 10px; border-radius: 6px; color: var(--primary-color); background: rgb(255 255 255 / 50%); position: absolute; bottom: 30px; left: 30px; backdrop-filter: blur(10px);">
            <h2>Upcoming Events</h2>
        </div>
        """
        for record in records:
            html_content += f"""
            <div style="background: red;">
                <p style="color: var(--primary-color); text-shadow: 2px 2px 2px rgba(255 255 255 / 80%);"><strong>{record.name}</strong></p>
                <p>Type: {record.type}</p>
                <p>Begin Date: {record.begin_date} at {record.begin_time}</p>
                <p>End Date: {record.end_date} at {record.end_time}</p>
                <p>Place: {record.place}</p>
                <p><a href="{record.link}" style="color: var(--primary-color); text-shadow: 2px 2px 2px rgba(255 255 255 / 80%);">More Info</a></p>
                <hr>
            </div>
            """
        self.setHtml(html_content)

