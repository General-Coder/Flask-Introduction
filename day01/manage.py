# from flask import Flask, render_template
from flask_script import Manager
from app import create_app

#实例化flask
# app = Flask(__name__)
app = create_app()

#实例化manager
manager = Manager(app=app)

#注册路由
# @app.route('/')
# #处理函数
# def hello_world():
#     return '<h1>Hello World!</h1>'
#
# @app.route('/index/')
# def index():
#     data = {
#         'msg':'给我份工作',
#         'data':'8k就可以'
#     }
#     return  render_template('one.html',**data)


#主函数
if __name__ == '__main__':
    #启动flask服务
    # app.run(
    #     host='0.0.0.0',
    #     port=12333,
    #     debug=True
    # )

    manager.run()