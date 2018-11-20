from flask import Flask
from .views import init_blue
from .ext import  init_ext
from .settings import conf

def create_app(evem):
    app = Flask(__name__)
    #初始化配置
    app.config.from_object(conf.get(evem,'debug'))
    #初始化第三方
    init_ext(app)
    #注册蓝图
    init_blue(app)
    return  app