from flask import Blueprint, render_template, request
from flask.json import jsonify
from app.ext import db
from app.ext import cache
from app.models import News
from tasks import task_one

blue = Blueprint('first',__name__)

@blue.route('/create_data/')
def create_data():
    datas = []
    for i in range(101):
        tmp = News(
            title='震惊' + str(i + 1)  + '下课是不可能',
            content='假设这里有料' + str(i + 1)
        )
        datas.append(tmp)
    db.session.add_all(datas)
    db.session.commit()
    return 'Create Success'


@blue.route('/')
@cache.cached(timeout=20)
def index():
    #解析参数
    print('进入函数')
    params = request.args
    page = int(params.get('page',1))
    per_page = int(params.get('per_page',15))
    pagination = News.query.paginate(page,per_page,error_out=False)
    data = {
        'news':pagination.items,
        'pagination':pagination
    }
    return render_template('app/index.html', **data)

@blue.route('/cache/')
def my_cache():
    #先获取ip，拼接我们的key
    ip = request.remote_addr
    key = ip + 'day04'
    #去缓存尝试拿数据
    data = cache.get(key)
    if data:
        print('有数据')
        return jsonify(data)
    else:
        # 一顿查数据
        new_data = {
            'code':1,
            'msg':'ok',
            'data':'呵呵哒'
        }
        print('查数据')
        cache.set(key,new_data,30)
        return jsonify(new_data)

@blue.before_request
def heheda():
    #反爬虫 首先检查有没有user-agent 再看ip如果在30s内访问10次 就搞他
    user_agent = request.user_agent
    if not user_agent:
        return jsonify({'code':10000,'msg':'h换个网站吧'}),500
    ip = request.remote_addr
    key = ip + 'fanpa'
    times = cache.get(key)
    if not times:
        cache.set(key,1,30)
    else:
        if int(times) >= 3:
            return '搞你M啊',404
        else:
            cache.set(key,times+1,30)

@blue.route('/hello/')
def hello():
    task_one.delay()
    return 'hello flask'


