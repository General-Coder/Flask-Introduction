from .views import blue
from .form import submit



def init_blue(app):
    app.register_blueprint(blue)
    app.register_blueprint(submit)


