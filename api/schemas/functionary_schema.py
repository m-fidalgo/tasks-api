from api import ma
from marshmallow import fields
from ..models import functionary_model

class FunctionarySchema(ma.ModelSchema):
  class Meta:
    model = functionary_model.Functionary
    fields = ("id", "name", "age", "projects", "_links")

  title = fields.String(required=True)
  description = fields.Integer(required=True)
  _links = ma.Hyperlinks(
    {
      "get": ma.URLFor("functionarydetail", id="<id>"),
      "put": ma.URLFor("functionarydetail", id="<id>"),
      "delete": ma.URLFor("functionarydetail", id="<id>")
    }
  )