# from celery import Celery
# from flask import render_template
# from flask_mail import Message
# from app.ext import mail,cache
# app = Celery(__name__)
# app.config_from_object('celery_conf')
#
# @app.task
# def send_email(reciver,url,u_id):
#     title= '欢迎注册爱鲜蜂后台管理'
#     msg = Message(title,[reciver],sender='17625904460@163.com')
#     msg.html = render_template('register/active.html', url=url)
#     mail.send(msg)
#     #设置缓存
#     key = url.split('/')[-1]
#     cache.set(key,u_id,timeout=60*10)