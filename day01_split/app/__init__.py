from flask import Flask
from .views import *

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'guanfang'
    app.register_blueprint(blueprint=blue)
    return  app
