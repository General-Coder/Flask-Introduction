from app.home import views




def init_blue_home(app):
    app.register_blueprint(views.home)

