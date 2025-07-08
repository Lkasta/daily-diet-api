from database import db
from sqlalchemy.sql import func

class Diet(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(300), nullable=False)
  date_time = db.Column(db.DateTime, nullable=False)
  within_diet = db.Column(db.Boolean, default=False)
