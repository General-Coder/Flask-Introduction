from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import  Migrate
from flask_session import Session
from  flask_sqlalchemy import SQLAlchemy
from app.settings import CACHE
from  celery import Celery



db = SQLAlchemy()
cache = Cache(config=CACHE.get('default'))
migrate = Migrate()
mail = Mail()



def init_ext(app):
    Session(app)
    migrate.init_app(app=app, db=db)
    db.init_app(app)
    cache.init_app(app)
    mail.init_app(app)
