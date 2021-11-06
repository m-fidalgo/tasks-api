from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required
from ..schemas import project_schema
from ..entities import project
from ..services import project_service
from ..pagination import paginate
from ..models import project_model

# List: métodos que não precisam de param pra funcionar
class ProjectList(Resource):
  def get(self):
    """
    Rota responsável por retornar todos os projetos
    ---
    responses:
      200:
        description: Lista de todos os projetos
        schema:
          id: Project
          properties:
            project_id:
              type: integer
            name:
              type: string
            description:
              type: string
            tasks:
              type: object
            functionaries:
              type: object
    """
    #projects = project_service.get_projects()
    ps = project_schema.ProjectSchema(many=True)
    return paginate(project_model.Project, ps)

  @jwt_required
  def post(self):
    """
    Rota responsável por cadastrar um novo projeto
    ---
    parameters:
      - in: header
        name: Authorization
        type: string
        required: true
      - in: body
        name: Project
        description: Criar novo projeto
        schema:
          type: object
          required:
            - name
            - description
            - tasks
            - functionaries
          properties:
            name:
              type: string
            description:
              type: string
            tasks:
              type: object
            functionaries:
              type: object
    responses:
      201:
        description: Projeto criado com sucesso
        schema:
          id: Project
          properties:
            project_id:
              type: integer
            name:
              type: string
            description:
              type: string
            tasks:
              type: object
            functionaries:
              type: object
      400:
        description: Erro de validação
    """
    ps = project_schema.ProjectSchema()
    validate = ps.validate(request.json)
    if validate:
      return make_response(jsonify(validate), 400)
    else:
      name = request.json["name"]
      description = request.json["description"]
      funcs = request.json["functionaries"]
      new_project = project.Project(name=name, description=description, functionaries=funcs)
      result = project_service.insert_project(new_project)
      return make_response(ps.jsonify(result), 201)

# Detail: métodos que recebem param
class ProjectDetail(Resource):
  def get(self, id):
    """
    Rota responsável por retornar um projeto com base em seu id
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Projeto encontrado
        schema:
          id: Project
          properties:
            project_id:
              type: integer
            name:
              type: string
            description:
              type: string
            tasks:
              type: object
            functionaries:
              type: object
    """
    project = project_service.get_project_by_id(id)
    if project is None:
      return make_response(jsonify("Project not found"), 404)
    ps = project_schema.ProjectSchema()
    return make_response(ps.jsonify(project), 200)

  @jwt_required
  def put(self, id):
    """
    Rota responsável por alterar projeto com base em seu id
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
        name: Project
        description: Alterar projeto
        schema:
          type: object
          required:
            - name
            - description
            - tasks
            - functionaries
          properties:
            name:
              type: string
            description:
              type: string
            tasks:
              type: object
            functionaries:
              type: object
    responses:
      200:
        description: Projeto alterado com sucesso
        schema:
          id: Project
          properties:
            project_id:
              type: integer
            name:
              type: string
            description:
              type: string
            tasks:
              type: object
            functionaries:
              type: object
      400:
        description: Erro de validação
      404:
        description: Projeto não encontrado
    """
    db_project = project_service.get_project_by_id(id)
    if db_project is None:
      return make_response(jsonify("Project not found"), 404)
    ps = project_schema.ProjectSchema()
    validate = ps.validate(request.json)
    if validate:
      return make_response(jsonify(validate), 400)
    else:
      name = request.json["name"]
      description = request.json["description"]
      funcs = request.json["functionaries"]
      new_project = project.Project(name=name, description=description, functionaries=funcs)
      project_service.update_project(db_project, new_project)
      updated_project = project_service.get_project_by_id(id)
      return make_response(ps.jsonify(updated_project), 200)

  @jwt_required
  def delete(self, id):
    """
    Rota responsável por excluir um projeto a partir de seu id
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
        description: Projeto deletado com sucesso
      404:
        description: Projeto não encontrado
    """
    project = project_service.get_project_by_id(id)
    if project is None:
      return make_response(jsonify("Project not found"), 404)
    project_service.delete_project(project)
    return make_response('', 204)

# adicionando recurso à api, nessa rota
api.add_resource(ProjectList, '/projects')
api.add_resource(ProjectDetail, '/projects/<int:id>')