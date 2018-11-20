from flask import Blueprint, request, render_template, redirect, flash
from flask_wtf import FlaskForm
from wtforms import PasswordField, validators, StringField, SubmitField

submit = Blueprint('form', __name__)


class LoginForm(FlaskForm):
    username = StringField(
        '用户名',
        [validators.DataRequired()]
    )
    password = PasswordField(
        '密码',
        [validators.DataRequired()]
    )
    password1 = PasswordField(
        '确认密码',
        [validators.DataRequired(), validators.EqualTo('password', '密码输入不一致')]
    )
    submit = SubmitField(
        '提交'
    )


@submit.route('/form/', methods=['GET', 'POST'])
def form_submit():
    login_form = LoginForm()
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        password1 = request.form.get('password1')
        if login_form.validate_on_submit():
            print(username)
            return 'success'
        else:
            flash('参数有误')
    return render_template('form/index.html',form=login_form)

