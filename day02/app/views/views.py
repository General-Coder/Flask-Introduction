import os
from app.models import db, Person
from flask import Blueprint, session, render_template
from jinja2 import Template

blue = Blueprint(
    name='bp',
    import_name=__name__
)


@blue.route('/set/')
def set_session():
    session['name'] = 'daShaDiao'
    return 'ok'


@blue.route('/get/')
def get_session():
    session.get('name', '游客')
    return 'ok'


@blue.route('/index/')
def index():
    path = r'/home/zd/flask/day02/app/templates/index.html'
    with open(path, 'r') as f:
        template = Template(f.read())
        html = template.render()
        return html


@blue.route('/test/')
def test():
    return render_template('test.html')


@blue.route('/macho/')
def macho():
    data = ['Python', 'php', 'C', 'C++', 'Java', 'C#', 'OC', 'R', 'GO']
    return render_template('macho.html', data=data)


@blue.route('/for/')
def for_demo():
    data = ['Python', 'php', 'C', 'C++', 'Java', 'C#', 'OC', 'R', 'GO']
    return render_template('foedemo.html', data=data)


@blue.route('/create/')
def create_db():
    db.create_all()
    return '创建完毕'


@blue.route('/drop/')
def drop_all():
    db.drop_all()
    return '跑路'


@blue.route('/create_data/')
def create_user():
    u = Person(
        name='张三'
    )
    db.session.add(u)
    db.session.commit()
    return '创建完毕'


@blue.route('/create_many/')
def create_many():
    persons = []
    for i in range(10):
        u = Person(name='张三' + str(i), age=i + 1)
        persons.append(u)
    db.session.add_all(persons)
    db.session.commit()
    return '创建完毕'


@blue.route('/get_users/')
def get_users():
    res = Person.query.all()
    for i in res:
        print(i.name)
    return '查询完毕'
