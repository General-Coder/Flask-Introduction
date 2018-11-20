from flask import Flask
from app.restful import init_api
from app.views import init_blue
from .ext import init_ext
from .settings import conf,template_folder,static_folder



def create_app(env):
    app = Flask(__name__,template_folder=template_folder,static_folder=static_folder)
    app.config.from_object(conf.get(env))
    init_ext(app)
    init_blue(app)
    init_api(app)
    return  app