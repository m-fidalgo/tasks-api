from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import user_schema
from ..entities import user
from ..services import user_service

class UserList(Resource):
  def post(self):
    us = user_schema.UserSchema()
    validate = us.validate(request.json)
    if validate:
      return make_response(jsonify(validate), 400)
    else:
      name = request.json["name"]
      email = request.json["email"]
      password = request.json["password"]
      new_user = user.User(name=name, email=email, password=password)
      result = user_service.insert_user(new_user)
      return make_response(us.jsonify(result), 201)

api.add_resource(UserList, '/users')