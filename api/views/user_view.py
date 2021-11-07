from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import user_schema
from ..entities import user
from ..services import user_service

class UserList(Resource):
  def post(self):
    """
    Rota responsável por cadastrar um usuário
    ---
    parameters:
      - in: body
        name: User
        description: Criar novo usuário
        schema:
          type: object
          required:
            - name
            - email
            - password
            - is_admin
          properties:
            name:
              type: string
            email:
              type: string
            password:
              type: string
            is_admin:
              type: boolean
    responses:
      201:
        description: Usuário criado com sucesso
        schema:
          id: User
          properties:
            user_id:
              type: integer
            name:
              type: string
            email:
              type: string
            password:
              type: string
            is_admin:
              type: boolean
      400:
        description: Erro de validação
    """
    us = user_schema.UserSchema()
    validate = us.validate(request.json)
    if validate:
      return make_response(jsonify(validate), 400)
    else:
      name = request.json["name"]
      email = request.json["email"]
      password = request.json["password"]
      is_admin = request.json["is_admin"]
      new_user = user.User(name=name, email=email, password=password, is_admin=is_admin)
      result = user_service.insert_user(new_user)
      return make_response(us.jsonify(result), 201)

api.add_resource(UserList, '/users')