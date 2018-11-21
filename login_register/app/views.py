from flask import Blueprint, request, flash, render_template
from .models import *

blue = Blueprint('blue', __name__)


def init_blue(app):
    app.register_blueprint(blue)


@blue.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html', form=form)

    elif request.method == 'POST':
        form = RegisterForm(request.form)
        if form.validate():
            print('登陆成功')
        else:
            print(form.errors,'错误信息')
        return render_template('register.html',form=form)

