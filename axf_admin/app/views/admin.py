from flask import Blueprint, render_template, request, redirect, g
from app.util import *
from app.ext import cache
from app.models import *

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():

    return render_template('base/base_main.html')


@blue.route('/item/')
def item():

    goods = Goods.query.filter(Goods.is_delete == 0)
    per_page = int(request.args.get('per_page', 15))
    page = int(request.args.get('page', 1))
    pagination = goods.paginate(page=page, per_page=per_page)
    return render_template('item/item.html', pagination=pagination, show=True)


@blue.route('/order_manage/')
def order_manage():
    status_map = {
        1:'待付款',
        2:'已付款',
        3:'已发货',
        4:'已收货',
        5:'待评价',
        6:'已评价',
    }
    all_orders = Order.query.all()
    for i in all_orders:
        i.created_time = i.create_time.strftime('%Y年%m月%d日 %H:%M:%S')
        sum_money = 0
        #算钱
        for j in i.order_items:
            sum_money += j.num * j.buy_money
        i.sum_money = sum_money
        #将订单的状态的数字变成文字
        i.ch_status = status_map.get(i.status)

    return render_template('order/order_index.html',all_orders=all_orders)


@blue.route('/nosale/')
def no_sale():
    res = get_no_sale()
    return render_template('no_sale/no_sale.html',res = res)


@blue.route('/auto_bh/')
def auto_bh():
    get_data()
    return render_template('auto/auto.html')


@blue.route('/index/')
def login():
    return render_template('index/index.html')


@blue.route('/register/')
def register():
    return render_template('register/register.html')


@blue.route('/active/<string:str>')
def active(str):
    u_id = cache.get(str)
    user = User.query.get(u_id)
    if user:
        user.is_active = True
        db.session.add(user)
        db.session.commit()
        return redirect('/index/')
    else:
        return redirect('/register/')


@blue.route('/item_search/')
def item_search():
    # 解析参数
    kw = request.args.get('kw')
    goods = Goods.query.filter(Goods.productlongname.contains(kw)).filter(Goods.is_delete == 0)
    per_page = int(request.args.get('per_page', 8))
    page = int(request.args.get('page', 1))
    pagination = goods.paginate(page=page, per_page=per_page)
    return render_template('item/item.html', pagination=pagination, kw=kw)
