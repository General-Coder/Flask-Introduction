from flask import Blueprint, request, jsonify
from app.ext import *
from app.models import *
from flask_restful import Resource


blue = Blueprint('restful', __name__)


@blue.route('/')
def hello():
    return {'ok':1}


@blue.errorhandler(404)
def my_404():
    return '资源不存在'


@blue.route('/news/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def news_api():
    if request.method == 'GET':
        id = int(request.args.get('id', 1))
        news = News.query.get_or_404(id)
        result = {
            'code': 1,
            'msg': 'ok',
            'data': news.model_to_dict()
        }
        return jsonify(result), 200
    elif request.method == 'POST':
        params = request.form
        title = params.get('title')
        content = params.get('content')
        news = News(
            title=title,
            content=content
        )
        db.session.add(news)
        db.session.commit()
        result = {
            'code': 1,
            'msg': 'add success',
            'data': news.model_to_dict()
        }
        return jsonify(result), 201
    elif request.method == 'PUT':
        params = request.form
        id = int(params.get('id'))
        news = News.query.get_or_404(id)
        title = params.get('title', news.title)
        content = params.get('content', news.content)
        news.content = content
        news.title = title
        db.session.add(news)
        db.session.commit()
        result = {
            'code': 1,
            'msg': 'modify success',
            'data': news.model_to_dict()
        }
        return jsonify(result), 201
    elif request.method == 'DELETE':
        id = int(request.form.get('id'))
        news = News.query.get_or_404(id)
        result = {
            'code': 1,
            'msg': 'delete success',
            'data': news.model_to_dict()
        }
        db.session.delete(news)
        db.session.commit()
        return jsonify(result), 204
    else:
        result = {
            'code': 2,
            'msg': 'method error',
        }
        return jsonify(result), 405


class NewsApiTest(Resource):

    def get(self):
        return {'data':'么么哒'}

api.add_resource(NewsApiTest,'/test/','/heheda/')



