from flask import Flask
from .views.views import blue
from flask_session import Session
from redis import StrictRedis
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234567980dsjhkfcndkvmndfklgsdg'
    # 指定sessio存储方案
    app.config['SESSION_TYPE'] = 'redis'  # 指定存储方案
    app.config['SESSION_KEY_PREFIX'] = 'zd:'  # 设置缓存的开头
    # 定制化存储到redis制定操作
    app.config['SESSION_REDIS'] = StrictRedis(host='127.0.0.1',db=6)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zd:zhangding@101.132.145.148:3306/flask02'
    # 实例化
    sess = Session()
    sess.init_app(app)
    app.register_blueprint(blueprint=blue)
    db.init_app(app)
    return app
