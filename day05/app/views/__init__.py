from .restful import blue

def init_blue(app):
    app.register_blueprint(blue)