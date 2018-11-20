from flask import Blueprint, request, render_template, jsonify, json
from sqlalchemy import or_, not_
from .ext import db
from .models import *

blue = Blueprint('first', __name__)


def init_blue(app):
    app.register_blueprint(blue)


# 捕获404信息
@blue.errorhandler(404)
def my_404(e):
    return '资源不存在'


@blue.route('/')
def hello():
    data = {
        'code': 1,
        'msg': 'ok'
    }
    json_data = jsonify(data)
    return json_data


@blue.route('/create_dog/')
def create_dog():
    # 批量创建dog数据
    dogs = []
    for i in range(50):
        dog = Dog()
        dog.name = '泰迪' + str(i + 1)
        dog.place = '九堡一区{num}户'.format(num=i + 1)
        dogs.append(dog)
    db.session.add_all(dogs)
    db.session.commit()
    return 'Create Dogs Success'


@blue.route('/delete_dog/<int:id>/')
def delete_dog(id):
    dog = Dog.query.filter_by(id=id).first_or_404()
    db.session.delete(dog)
    db.session.commit()
    return 'Delete Success'


@blue.route('/get_dogs/')
def get_dogs():
    params = request.args
    # id大于20的数据
    # dogs = Dog.query.filter(Dog.id.__gt__(20))
    # name=泰迪9的数据
    dogs = Dog.query.filter(Dog.name == '泰迪10')
    # 过去名字包含34的
    dogs = Dog.query.filter(Dog.name.contains('34'))
    # 获取id是9 10 11的数据
    dogs = Dog.query.filter(Dog.id.in_([9, 10, 11]))
    # 查找name以4结尾的数据
    # dogs = Dog.query.filter(Dog.name.like('%4_'))
    dogs = Dog.query.filter(Dog.name.endswith('4'))
    # get只能通过主键去搜索
    dog = Dog.query.get(5)
    # 跳过1条数据最多取3条数据
    # dogs = dogs.offset(1).limit(3)
    dogs = dogs.order_by('-id').offset(2)
    return render_template('datas.html', dogs=dogs)


@blue.route('/page/')
def get_page_data():
    # 获得数据集
    dogs = Dog.query.filter(Dog.id.__gt__(1))
    # 获得当前页码
    current_page = int(request.args.get('page', 1))
    # 每一页多少数据
    per_page = int(request.args.get('per', 5))
    # 获得分页对象
    pagination = dogs.paginate(current_page, per_page)
    # datas = dogs.offset((current_page - 1) * per_page).limit(per_page)
    # return render_template('datas.html', dogs=paginates.items)
    dogs_data = [i.to_dict() for i in pagination.items]
    data = {
        'code': 1,
        'msg': 'ok',
        'data': {
            'dogs': dogs_data,
            'per_page':pagination.per_page,
            'pages': pagination.pages,
            'prev_num': pagination.prev_num,
            'has_prev': pagination.has_prev,
            'next_num': pagination.next_num,
            'has_next': pagination.has_next,
            'current_page': pagination.page,
            'page_range': list(range(1,pagination.pages+1))
        }
    }
    return render_template('page.html', datas=data)


@blue.route('/query/')
def my_query():
    # dogs = Dog.query.filter(or_(Dog.name.contains('尼克'),Dog.name.contains('4')))
    dogs = Dog.query.filter(not_(Dog.name.contains('尼克')))
    return render_template('datas.html', dogs=dogs)


@blue.route('/get_grade/<int:s_id>/')
def get_grade_by_stu(s_id):
    # 先查询学生
    stu = Stu.query.get(s_id)
    # 通过学生查班级
    # grade = Grade.query.get(stu.grade)
    grade = stu.grades
    return grade.name


@blue.route('/get_stu/<int:g_id>/')
def get_stu_by_grade(g_id):
    # 先查询班级
    # stu = Stu.query.filter(Stu.grade==g_id)
    stu = Grade.query.get(g_id).stus
    # 通过学生查班级
    for i in stu:
        print(i.name)
    return 'ok'


@blue.route('/create_data/')
def create_my_data():
    tag1 = Tag(title='python')
    tag2 = Tag(title='java')
    db.session.add_all([tag1, tag2])
    db.session.commit()

    book1 = Book(name='python黑客攻防')
    book2 = Book(name='java弃疗指导')
    book1.tags.append(tag1)
    book1.tags.append(tag2)
    book2.tags = [tag1, tag2]
    db.session.add_all([book1, book2])
    db.session.commit()
    return 'Create Success'


@blue.route('/get_book/<int:t_id>')
def get_book_by_tag(t_id):
    # 查tag
    tag = Tag.query.get(t_id)
    books = tag.books
    for i in books:
        print(i.name)
    return 'ok'


@blue.route('/get_tag/<int:b_id>')
def get_tag_by_book(b_id):
    # 查tag
    book = Book.query.get(b_id)
    tags = book.tags
    for i in tags:
        print(i.title)
    return 'ok'


@blue.route('/get_phone/<int:x_id>/')
def get_phone_by_xin(x_id):
    phone = Phone.query.filter(Phone.u_id==x_id)
    for i in phone:
        print(i.name)
    return 'ok'

@blue.route('/get_u/<int:p_id>/')
def get_u_by_phone(p_id):
    phone = Phone.query.get(p_id)
    u = Xin.query.get(phone.u_id)
    print(u.name)
    return 'ok'

@blue.route('/get_phone_v1/<int:x_id>/')
def get_phone(x_id):
    phone = Xin.query.get(x_id).phones
    for i in phone:
        print(i.name)
    return 'ok'

@blue.route('/get_u_v1/<int:p_id>/')
def get_u(p_id):
    xin = Phone.query.get(p_id).u
    print(xin.name)
    return 'ok'
