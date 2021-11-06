from ..models import user_model
from api import db

def insert_user(user):
  db_user = user_model.User(name=user.name, email=user.email, password=user.password)
  db_user.gen_password()
  db.session.add(db_user)
  db.session.commit()
  return db_user

def get_user_email(email):
  return user_model.User.query.filter_by(email=email).first()