from application import db
from datetime import datetime 

class tasks(db.model):
    id = db.column(db.Integer, primary_key=True)
    description = db.column(db.string(35), nullable=False)
    completed = db.column(Boolean, nullable=False, default=False)
    date_created = db.column(db.datetime, nullable=False, default=datetime.utcnow)
    