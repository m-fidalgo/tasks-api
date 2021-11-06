from ..models import project_model
from api import db

def insert_project(project):
  db_project = project_model.Project(name=project.name, description=project.description)
  db.session.add(db_project)
  db.session.commit()
  return db_project

def get_projects():
  projects = project_model.Project.query.all()
  return projects

def get_project_by_id(id):
  project = project_model.Project.query.filter_by(id=id).first()
  return project

def update_project(project, new_project):
  project.name = new_project.name
  project.description = new_project.description
  db.session.commit()

def delete_project(project):
  db.session.delete(project)
  db.session.commit()