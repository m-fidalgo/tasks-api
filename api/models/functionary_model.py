from api import db

class Functionary(db.Model):
  __tablename__ = "functionary"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  name = db.Column(db.String(50), nullable=False)
  age = db.Column(db.Integer, nullable=False)