from flask import Flask
from  .views import *

def create_app():
    #创建APP flask的实例
    app = Flask(__name__)
    #注册蓝图
    app.register_blueprint(blueprint=blue)
    #返回app
    return  app