from app.views.admin import blue


def init_blue(app):
    app.register_blueprint(blue)