from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
JWTManager(app)

api = Api(app)
swagger = Swagger(app)

from .views import task_view, project_view, functionary_view, user_view, login_view, refresh_token_view
from .models import task_model, project_model, functionary_model, user_model
