from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import project_schema
from ..entities import project
from ..services import project_service
from ..pagination import paginate
from ..models import project_model

# List: métodos que não precisam de param pra funcionar
class ProjectList(Resource):
  def get(self):
    #projects = project_service.get_projects()
    ps = project_schema.ProjectSchema(many=True)
    return paginate(project_model.Project, ps)

  def post(self):
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
    project = project_service.get_project_by_id(id)
    if project is None:
      return make_response(jsonify("Project not found"), 404)
    ps = project_schema.ProjectSchema()
    return make_response(ps.jsonify(project), 200)

  def put(self, id):
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
      return make_response(ps.jsonify(updated_project), 201)

  def delete(self, id):
    project = project_service.get_project_by_id(id)
    if project is None:
      return make_response(jsonify("Project not found"), 404)
    project_service.delete_project(project)
    return make_response('', 204)

# adicionando recurso à api, nessa rota
api.add_resource(ProjectList, '/projects')
api.add_resource(ProjectDetail, '/projects/<int:id>')