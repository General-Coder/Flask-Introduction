from flask import request, render_template, g
from flask_mail import Message
from flask_restful import Resource, marshal_with
from app.ext import mail, cache, db
from app.util import *
from app.models import User, Goods, Order
from .args import *
from .fields import *


class RegisterAPI(Resource):
    @marshal_with(public_fileds)
    def post(self):
        params = register_args.parse_args()
        email = params.get('email')
        pwd = params.get('pwd')
        confirm_pwd = params.get('confirm_pwd')
        # 判断密码和确认密码是否一致
        if pwd != confirm_pwd:
            return {'code': 2, 'msg': '密码不一致'}
        res = User.create_user(email=email, pwd=pwd)
        # 发送邮件,激活
        url = 'http://' + request.host + '/active/' + create_unique_str()
        if res:
            # send_email.delay(email, url, res.id)
            title = '欢迎注册爱鲜蜂后台管理'
            msg = Message(title, [email], sender='17625904460@163.com')
            msg.html = render_template('register/active.html', url=url)
            mail.send(msg)
            # 设置缓存
            key = url.split('/')[-1]
            cache.set(key, res.id, timeout=60 * 60)
            return {'data': '/index/'}
        else:
            return {'code': 3, 'msg': '注册失败,邮箱已被使用'}


class LoginAPI(Resource):

    @marshal_with(public_fileds)
    def post(self):
        params = login_args.parse_args()
        email = params.get('email')
        pwd = params.get('pwd')
        user = User.query.filter(User.email == email).first()
        if not user:
            return {'code': 2, 'msg': '账号不存在'}
        else:
            if user.is_active == False:
                return {'code': 3, 'msg': '账号未激活'}
            else:
                if user.pwd == enc_pwd(pwd):

                    return {'data': '/item/'}
                else:
                    return {'code': 4, 'msg': '密码错误'}


class DeleteDataAPI(Resource):

    @marshal_with(public_fileds)
    def delete(self):
        params = delete_args.parse_args()
        c_id = params.get('c_id')
        goods = Goods.query.filter_by(productid=c_id).first()
        goods.is_delete = 1
        db.session.add(goods)
        db.session.commit()
        return {'msg': '删除成功'}


class ChangeDataAPI(Resource):

    @marshal_with(public_fileds)
    def patch(self):
        params = change_args.parse_args()
        c_id = params.get('c_id')
        longname = params.get('longname')
        fics = params.get('fics')
        price = params.get('price')
        mprice = params.get('mprice')
        nums = params.get('nums')
        goods = Goods.query.get(c_id)
        goods.productlongname = longname if longname else goods.productlongname
        goods.specifics = fics if fics else goods.specifics
        goods.price = price if price else goods.price
        goods.marketprice = mprice if mprice else goods.marketprice
        goods.storenums = nums if nums else goods.storenums
        db.session.add(goods)
        db.session.commit()
        return {'msg': '修改成功', 'data': '/item/'}


class StatusAPI(Resource):
    @marshal_with(public_fileds)
    def patch(self):
        params = status_args.parse_args()
        o_id = params.get('o_id')
        status = params.get('status')
        order = Order.query.get(o_id)
        order.status = status
        db.session.add(order)
        db.session.commit()
        return {}
