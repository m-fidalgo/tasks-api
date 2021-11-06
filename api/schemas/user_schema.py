from api import ma
from marshmallow import fields
from ..models import user_model

class UserSchema(ma.ModelSchema):
  class Meta:
    model = user_model.User
    fields = ("id", "name", "email", "password")

  name = fields.String(required=True)
  email = fields.String(required=True)
  password = fields.String(required=True)