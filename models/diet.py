from database import db
from datetime import datetime

class Diet(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(300), default=datetime.utcnow)
  date_time = db.Column(db.DateTime, nullable=False)
  within_diet = db.Column(db.Boolean, default=False )
