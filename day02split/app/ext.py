from flask_session import  Session
from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()

def init_ext(app):
    se = Session()
    se.init_app(app)
    #db绑定
    db.init_app(app)