from flask_bootstrap import Bootstrap
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate


db = SQLAlchemy()



def init_ext(app):
    sess = Session()
    db.init_app(app)
    sess.init_app(app)
    Bootstrap(app)
    #实例化migrate
    migrate = Migrate(app=app,db=db)

