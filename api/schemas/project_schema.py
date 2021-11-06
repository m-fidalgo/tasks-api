from api import ma
from ..models import project_model
from marshmallow import fields

# serialização e desserialização
class ProjectSchema(ma.ModelSchema):
  class Meta:
    model = project_model.Project
    fields = ("id", "name", "description", "tasks", "functionaries")

  name = fields.String(required=True)
  description = fields.String(required=True)