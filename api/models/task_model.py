from sqlalchemy.orm import backref
from api import db
from .project_model import Project

class Task(db.Model):
  __tablename__ = "task"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  title = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(100), nullable=False)
  expiration_date = db.Column(db.Date, nullable=False)

  project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
  project = db.relationship(Project, backref=db.backref("tasks", lazy="dynamic"))
