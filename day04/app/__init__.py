from flask import Flask
from .views import init_blue
from .ext import init_ext
from .settings import *

def create_app(enev):
    app = Flask(__name__,template_folder=template_folder,static_folder=static_folder)
    app.config.from_object(conf.get(enev))
    init_ext(app)
    init_blue(app)

    return app