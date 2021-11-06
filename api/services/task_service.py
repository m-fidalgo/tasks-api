from ..models import task_model
from api import db

def insert_task(task):
  db_task = task_model.Task(title=task.title, description=task.description, expiration_date=task.expiration_date)
  db.session.add(db_task)
  db.session.commit()
  return db_task