from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta
from ..schemas import login_schema
from ..services import user_service

class LoginList(Resource):
  def post(self):
    ls = login_schema.LoginSchema()
    validate = ls.validate(request.json)
    if validate:
      return make_response(jsonify(validate), 400)
    else:
      email = request.json["email"]
      password = request.json["password"]
      db_user = user_service.get_user_email(email)
      if db_user and db_user.get_password(password):
        #gerar access token
        access_token = create_access_token(
          identity=db_user.id,
          expires_delta=timedelta(seconds=120)
        )

        refresh_token = create_refresh_token(identity=db_user.id)

        return make_response(jsonify({
          'access_token': access_token,
          'refresh_token': refresh_token,
          'message': 'Login successful'
        }), 200)
      return make_response(jsonify({
          'message': 'Invalid credentials'
        }), 401)

api.add_resource(LoginList, '/login')