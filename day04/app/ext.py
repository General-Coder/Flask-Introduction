from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache
from .settings import CACHE

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
cache = Cache(config=CACHE.get('default'))

def init_ext(app):
    Session(app)
    # debug = DebugToolbarExtension()
    bootstrap.init_app(app)
    migrate.init_app(app=app, db=db)
    # debug.init_app(app)
    db.init_app(app)
    cache.init_app(app)