from api import ma
from ..models import task_model
from marshmallow import fields

# serialização e desserialização
class TaskSchema(ma.ModelSchema):
  class Meta:
    model = task_model.Task
    fields = ("id", "title", "description", "expiration_date", "project", "_links")

  title = fields.String(required=True)
  description = fields.String(required=True)
  expiration_date = fields.Date(required=True)
  project = fields.String(required=True)
  _links = ma.Hyperlinks(
    {
      "get": ma.URLFor("taskdetail", id="<id>"),
      "put": ma.URLFor("taskdetail", id="<id>"),
      "delete": ma.URLFor("taskdetail", id="<id>")
    }
  )