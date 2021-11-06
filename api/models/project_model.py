from api import db

class Project(db.Model):
  __tablename__ = "project"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  name = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(100), nullable=False)