from  .urls import  api

def init_api(app):
    api.init_app(app)