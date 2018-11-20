from flask import make_response, json
from  flask_restful import Api
from app.views.api_v1 import *


api = Api()

# class MyApi(Api):
#     def __init__(self, *args, **kwargs):
#         super(Api, self).__init__(*args, **kwargs)
#         self.representations = {
#             'text/html': output_html,
#             'application/json': output_json,
#         }
# @api.representation('application/json')
# def output_json(data, code, headers=None):
#     resp = make_response(json.dumps(data), code)
#     resp.headers.extend(headers or {})
#     return resp


@api.representation('text/html')
def output_html(data, code, headers=None):
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp


def init_api(app):
    api.init_app(app)





#下边注册各种api
api.add_resource(NewOneApi,'/news/')
api.add_resource(TwoApi,'/two/')
api.add_resource(ThreeApi,'/three/<int:id>/')
api.add_resource(FourApi,'/four/<int:page>/<int:per_page>/')
api.add_resource(FiveApi,'/five/')
api.add_resource(SixApi,'/six/')
api.add_resource(SevenApi,'/seven/')
api.add_resource(TestApi,'/test/')
api.add_resource(LoginApi,'/login/')