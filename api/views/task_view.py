from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required
from ..schemas import task_schema
from ..entities import task
from ..services import task_service, project_service
from ..pagination import paginate
from ..models import task_model

# List: métodos que não precisam de param pra funcionar
class TaskList(Resource):
  @jwt_required
  def get(self):
    ts = task_schema.TaskSchema(many=True)
    return paginate(task_model.Task, ts)

  def post(self):
    ts = task_schema.TaskSchema()
    validate = ts.validate(request.json)

    # há erros de validação
    if validate:
      return make_response(jsonify(validate), 400)
    else:
      title = request.json["title"]
      description = request.json["description"]
      expiration_date = request.json["expiration_date"]
      project = request.json["project"]
      task_project = project_service.get_project_by_id(project)

      if task_project is None:
        return make_response(jsonify("Project not found"), 404)

      new_task = task.Task(title=title, description=description, expiration_date=expiration_date, project=task_project)
      result = task_service.insert_task(new_task)
      return make_response(ts.jsonify(result), 201)

# Detail: métodos que recebem param
class TaskDetail(Resource):
  def get(self, id):
    task = task_service.get_task_by_id(id)
    if task is None:
      return make_response(jsonify("Task not found"), 404)
    ts = task_schema.TaskSchema()
    return make_response(ts.jsonify(task), 200)

  def put(self, id):
    db_task = task_service.get_task_by_id(id)
    if db_task is None:
      return make_response(jsonify("Task not found"), 404)
    ts = task_schema.TaskSchema()
    validate = ts.validate(request.json)
    if validate:
      return make_response(jsonify(validate), 400)
    else:
      title = request.json["title"]
      description = request.json["description"]
      expiration_date = request.json["expiration_date"]
      project = request.json["project"]
      task_project = project_service.get_project_by_id(project)

      if task_project is None:
        return make_response(jsonify("Project not found"), 404)

      new_task = task.Task(title=title, description=description, expiration_date=expiration_date, project=task_project)
      task_service.update_task(db_task, new_task)
      updated_task = task_service.get_task_by_id(id)
      return make_response(ts.jsonify(updated_task), 201)

  def delete(self, id):
    task = task_service.get_task_by_id(id)
    if task is None:
      return make_response(jsonify("Task not found"), 404)
    task_service.delete_task(task)
    return make_response('', 204)

# adicionando recurso à api, nessa rota
api.add_resource(TaskList, '/tasks')
api.add_resource(TaskDetail, '/tasks/<int:id>')