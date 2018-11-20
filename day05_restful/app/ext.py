from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .settings import *


db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config=CACHE.get('default'))
sess = Session()
bootstrap = Bootstrap()


def init_ext(app):
    sess.init_app(app)
    db.init_app(app)
    migrate.init_app(app=app,db=db)
    cache.init_app(app)
    bootstrap.init_app(app)
