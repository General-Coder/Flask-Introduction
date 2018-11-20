from flask import Blueprint, json, Response
from  app.ext import db

blue = Blueprint('app',__name__)

def init_blue(app):
    app.register_blueprint(blue)

@blue.route('/json/')
def json666():
    result = json.jsonify({'name':'value'})
    # result = json.jsonify(name='value',age=18)
    # result = json.dumps({'name':'value','age':18})
    # print(result)
    # print(type(result))
    # result = "{'name:'tom'}"
    # response = Response(response=result,content_type='application/json')
    return  result
