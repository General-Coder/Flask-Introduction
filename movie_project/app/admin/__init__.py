from app.admin import views
from app.models import *


def init_blue_admin(app):
    app.register_blueprint(views.admin)