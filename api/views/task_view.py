from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_claims
from ..schemas import task_schema
from ..entities import task
from ..services import task_service, project_service
from ..pagination import paginate
from ..models import task_model
from ..decorators import admin_required, api_key_required

# List: métodos que não precisam de param pra funcionar
class TaskList(Resource):
  @api_key_required
  def get(self):
    """
    Rota responsável por retornar todas as tarefas
    ---
    responses:
      200:
        description: Lista de todas as tarefas
        schema:
          id: Task
          properties:
            task_id:
              type: integer
            title:
              type: string
            description:
              type: string
            expiration_date:
              type: string
            project:
              type: string
    """
    ts = task_schema.TaskSchema(many=True)
    return paginate(task_model.Task, ts)

  @jwt_required
  def post(self):
    """
    Rota responsável por cadastrar uma nova tarefa
    ---
    parameters:
      - in: header
        name: Authorization
        type: string
        required: true
      - in: body
        name: Task
        description: Criar nova tarefa
        schema:
          type: object
          required:
            - title
            - description
            - expiration_date
            - project
          properties:
            title:
              type: string
            description:
              type: string
            expiration_date:
              type: string
            project:
              type: string
    responses:
      201: 
        description: Tarefa criada com sucesso
        schema:
          id: Task
          properties:
            task_id:
              type: integer
            title:
              type: string
            description:
              type: string
            expiration_date:
              type: string
            project:
              type: string
      400:
        description: Erros de validação
      404:
        descriprion: Projeto não encontrado
    """
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
  @api_key_required
  def get(self, id):
    """
    Rota responsável por exibir uma tarefa a partir de seu id
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Tarefa encontrada
        schema:
          id: Task
          properties:
            task_id:
              type: integer
            title:
              type: string
            description:
              type: string
            expiration_date:
              type: string
            project:
              type: string
      404:
        description: Tarefa não encontrada
    """
    task = task_service.get_task_by_id(id)
    if task is None:
      return make_response(jsonify("Task not found"), 404)
    ts = task_schema.TaskSchema()
    return make_response(ts.jsonify(task), 200)

  @jwt_required
  def put(self, id):
    """
    Rota responsável por alterar uma tarefa
    ---
    parameters:
      - in: header
        name: Authorization
        type: string
        required: true
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: Task
        description: Alterar tarefa
        schema:
          type: object
          required:
            - title
            - description
            - expiration_date
            - project
          properties:
            task_id:
              type: integer
            title:
              type: string
            description:
              type: string
            expiration_date:
              type: string
            project:
              type: string
    responses:
      200: 
        description: Tarefa alterada com sucesso
        schema:
          id: Task
          properties:
            title:
              type: string
            description:
              type: string
            expiration_date:
              type: string
            project:
              type: string
      404:
        description: Tarefa ou projeto não encontrado
      400:
        description: Erros de validação
    """
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
      return make_response(ts.jsonify(updated_task), 200)

  @admin_required
  def delete(self, id):
    """
    Rota responsável por excluir uma tarefa a partir de seu id
    ---
    parameters:
      - in: header
        name: Authorization
        type: string
        required: true
      - in: path
        name: id
        type: integer
        required: true
    responses:
      204:
        description: Tarefa deletada com sucesso
      403:
        description: O usuário não tem permissão para apagar a tarefa
      404:
        description: Tarefa não encontrada
    """
    task = task_service.get_task_by_id(id)
    if task is None:
      return make_response(jsonify("Task not found"), 404)
    task_service.delete_task(task)
    return make_response('', 204)

# adicionando recurso à api, nessa rota
api.add_resource(TaskList, '/tasks')
api.add_resource(TaskDetail, '/tasks/<int:id>')