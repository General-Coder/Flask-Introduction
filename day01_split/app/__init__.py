from flask import Flask
from flask_session import Session

from .views import *

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'guanfang'
    app.config['SESSION_TYPE'] = 'redis'
    Session(app=app)
    app.register_blueprint(blueprint=blue)
    return  app
