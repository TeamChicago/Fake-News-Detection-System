from model.app import db
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, Float


class News(db.Model):
    __tablename__='news'

    id = db.Column(db.Integer, primary_key=True, unique = True)
    text = db.Column(db.String(4096))
    # local_date_time = db.Column(DateTime(default=datetime.utcnow))
    reliability = db.Column(db.Float)

    def __init__(self, id, text, local_date_time, reliability):
        self.id = id
        self.text = text
        # self.local_date_time = local_date_time
        self.reliability = reliability

    def __repr__(self):
        return f"<News {self.text}>"