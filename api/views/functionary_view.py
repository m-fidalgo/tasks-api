from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_claims
from ..schemas import functionary_schema
from ..entities import functionary
from ..services import functionary_service
from ..pagination import paginate
from ..models import functionary_model
from ..decorators import admin_required, api_key_required

class FunctionaryList(Resource):
  @api_key_required
  def get(self):
    #funcs = functionary_service.get_funcs()
    fs = functionary_schema.FunctionarySchema(many=True)
    return paginate(functionary_model.Functionary, fs)
    #make_response(fs.jsonify(funcs), 200)

  @jwt_required
  def post(self):
    fs = functionary_schema.FunctionarySchema()
    validate = fs.validate(request.json)
    if validate:
      return make_response(jsonify(validate), 400)
    else:
      name = request.json["name"]
      age = request.json["age"]
      new_func = functionary.Functionary(name=name, age=age)
      result = functionary_service.insert_func(new_func)
      return make_response(fs.jsonify(result), 201)

class FunctionaryDetail(Resource):
  @api_key_required
  def get(self, id):
    func = functionary_service.get_func_by_id(id)
    if func is None:
      return make_response(jsonify("Functionary not found"), 404)
    fs = functionary_schema.FunctionarySchema()
    return make_response(fs.jsonify(func), 201)

  @jwt_required
  def put(self, id):
    func = functionary_service.get_func_by_id(id)
    if func is None:
      return make_response(jsonify("Functionary not found"), 404)
    fs = functionary_schema.FunctionarySchema()
    validate = fs.validate(request.json)
    if validate:
      return make_response(jsonify(validate), 400)
    else:
      name = request.json["name"]
      age = request.json["age"]
      new_func = functionary.Functionary(name=name, age=age)
      functionary_service.update_func(func, new_func)
      updated_func = functionary_service.get_func_by_id(id)
      return make_response(fs.jsonify(updated_func), 201)

  @admin_required
  def delete(self, id):
    func = functionary_service.get_func_by_id(id)
    if func is None:
      return make_response(jsonify("Functionary not found"), 404)
    functionary_service.delete_func(func)
    return make_response('', 204)

api.add_resource(FunctionaryList, '/functionaries')
api.add_resource(FunctionaryDetail, '/functionaries/<int:id>')