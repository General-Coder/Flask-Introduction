from flask import Flask
from app.urls_api_v1 import init_api
from .settings import *
from .views import *
from .ext import *

def create_app(env):
    app = Flask(__name__,template_folder=template_folder,static_folder=static_folder)
    app.config.from_object(conf.get(env))

    init_ext(app)
    init_api(app)


    return app
