from flask import Flask, render_template
from app.home import init_blue_home
from app.admin import init_blue_admin
from .settings import conf
from .ext import init_ext




def create_app():
    app = Flask(__name__)
    app.config.from_object(conf.get('debug'))
    init_ext(app)
    init_blue_home(app)
    init_blue_admin(app)

    @app.errorhandler(404)
    def my_404(error):
        return render_template('home/404.html'), 404

    return app