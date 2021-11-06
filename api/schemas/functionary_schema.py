from api import ma
from marshmallow import fields
from ..models import functionary_model

class FunctionarySchema(ma.ModelSchema):
  class Meta:
    model = functionary_model.Functionary
    fields = ("id", "name", "age")

  title = fields.String(required=True)
  description = fields.Integer(required=True)