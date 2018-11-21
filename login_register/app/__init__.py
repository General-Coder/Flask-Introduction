from  flask import  Flask
from .settings import DebugConfig
from .ext import  init_ext
from .views import init_blue

def create_app():
    app = Flask(__name__)
    app.config.from_object(DebugConfig)
    init_ext(app)
    init_blue(app)

    return app