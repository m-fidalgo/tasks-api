from ..models import functionary_model
from api import db

def insert_func(func):
  db_func = functionary_model.Functionary(name=func.name, age=func.age)
  db.session.add(db_func)
  db.session.commit()
  return db_func

def get_funcs():
  funcs = functionary_model.Functionary.query.all()
  return funcs

def get_func_by_id(id):
  func = functionary_model.Functionary.query.filter_by(id=id).first()
  return func

def update_func(func, new_func):
  func.name = new_func.name
  func.age = new_func.age
  db.session.commit()

def delete_func(func):
  db.session.delete(func)
  db.session.commit()