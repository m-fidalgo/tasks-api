from ..models import task_model
from api import db

def insert_task(task):
  db_task = task_model.Task(title=task.title, description=task.description, expiration_date=task.expiration_date)
  db.session.add(db_task)
  db.session.commit()
  return db_task

def get_tasks():
  tasks = task_model.Task.query.all()
  return tasks

def get_task_by_id(id):
  task = task_model.Task.query.filter_by(id=id).first()
  return task

def update_task(task, new_task):
  task.title = new_task.title
  task.description = new_task.description
  task.expiration_date = new_task.expiration_date
  db.session.commit()