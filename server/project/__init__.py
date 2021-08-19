from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from server.project.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# def create_app():
#   app = Flask(__name__)
#   app.config.from_object(DevelopmentConfig)
#
#   db.init_app(app)
#   bcrypt.init_app(app)
#
#   return app


