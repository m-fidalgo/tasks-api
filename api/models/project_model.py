from api import db
from .functionary_model import Functionary

func_project = db.Table("func_project",
  db.Column("project_id", db.Integer, db.ForeignKey('project.id'), primary_key=True, nullable=False),
  db.Column("func_id", db.Integer, db.ForeignKey('functionary.id'), primary_key=True, nullable=False))
  
class Project(db.Model):
  __tablename__ = "project"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  name = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(100), nullable=False)

  functionaries = db.relationship(Functionary, secondary="func_project", back_populates="projects")