from api import api
from flask_restful import Resource
from flask import  make_response, jsonify
from flask_jwt_extended import get_jwt_identity, create_refresh_token, create_access_token, jwt_refresh_token_required
from datetime import timedelta

class RefreshTokenList(Resource):
  @jwt_refresh_token_required
  def post(self):
    token_user = get_jwt_identity()
    access_token = create_access_token(
      identity=token_user,
      expires_delta=timedelta(seconds=120)
    )
    refresh_token = create_refresh_token(identity=token_user)

    return make_response(jsonify({
      'access_token': access_token,
      'refresh_token': refresh_token
    }), 200)

api.add_resource(RefreshTokenList, '/token/refresh')