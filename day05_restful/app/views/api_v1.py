from flask import request, jsonify, render_template
from flask_restful import Resource, marshal, marshal_with, reqparse
from app.fields_apis_v1 import *
from app.models import News
from app.args_apis_v1 import *
from app.sql_util import SqlTool


class NewOneApi(Resource):

    @marshal_with(one_fields)
    def get(self, *args, **kwargs):
        id = int(request.args.get('id'))
        news = News.query.get_or_404(id)
        return news


class TwoApi(Resource):

    @marshal_with(two_fields)
    def get(self):
        hobby = ['抽烟', '喝酒', '推车']
        return {'hobby': hobby, 'name': 'hehe'}


class ThreeApi(Resource):

    @marshal_with(three_fileds)
    def get(self, **kwargs):
        id = kwargs.get('id')
        news = News.query.get_or_404(id)
        return {'data': news}


class FourApi(Resource):

    @marshal_with(four_fields)
    def get(self, page, per_page):
        datas = News.query.paginate(
            page,
            per_page,
            error_out=False
        )
        return {'code': 2, 'data': datas.items}


class FiveApi(Resource):

    def get(self):
        my_args = my_params.parse_args()
        print(my_args, type(my_args))
        print(my_args.get('hobby'))
        return {'msg': 'ok'}


class SixApi(Resource):

    def get(self):
        args = two_args.parse_args()
        print(args)
        return {'msg': 'ok'}


    def post(self):
        args = two_args.parse_args()
        print(args)
        return {'ok': 1}


class SevenApi(Resource):

    def get(self):
        my_args = three_args.parse_args()
        print(my_args)
        return {'msg': 'ok'}


class TestApi(Resource):

    def get(self):
        tool = SqlTool(
            user='zd',
            pwd='zhangding',
            host='localhost',
            port=3306,
            db='flask04'
        )
        sql = 'select * from news;'
        res = tool.query(sql)
        print(res)
        return {'ok': 'hehe'}

class LoginApi(Resource):

    def get(self):
        return render_template('app/index.html')

    @marshal_with(login_fileds)
    def post(self):
        my_args = login_args.parse_args()
        pwd = my_args.get('pwd')
        pwd1 = my_args.get('pwd1')
        name = my_args.get('name')
        if name == 'zhangding' and pwd == pwd1 and pwd == '123456':
            return {}
        else:
            return {'code':2,'msg':'error'}

