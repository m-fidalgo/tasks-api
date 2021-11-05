from flask_restful import Resource
from api import api

# List: métodos que não precisam de param pra funcionar
class TaskList(Resource):
  def get(self):
    return "Hello world"

# adicionando recurso à api, nessa rota
api.add_resource(TaskList, '/tasks')