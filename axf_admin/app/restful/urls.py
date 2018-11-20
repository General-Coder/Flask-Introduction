from flask_restful import Api
from .apis import *

api = Api()

#下面写一堆路由

api.add_resource(RegisterAPI,'/register/')
api.add_resource(LoginAPI,'/index/')
api.add_resource(DeleteDataAPI,'/delete_data/')
api.add_resource(ChangeDataAPI,'/change_data/')