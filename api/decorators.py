from functools import wraps
from flask import make_response, jsonify, request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims
from .services import user_service

def admin_required(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    verify_jwt_in_request()
    claims = get_jwt_claims()
    if claims["roles"] != "admin":
      return make_response(jsonify("Not allowed"), 403)
    else:
      return fn(*args, **kwargs)
  return wrapper

def api_key_required(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    api_key = request.args.get("api_key")
    if api_key and user_service.get_user_api_key(api_key):
      return fn(*args, **kwargs)
    else:
      return make_response(jsonify("Not allowed"), 401)
  return wrapper