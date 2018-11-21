from wtforms import Form,StringField,PasswordField,validators
from .ext import db

class Myvalidators(object):
    '''自定义验证规则'''
    def __init__(self,message):
        self.message = message
    def __call__(self, form, field):
        print(field.data,"用户输入的信息")
        if field.data == "zhangding":
            return None
        raise validators.ValidationError(self.message)




class RegisterForm(Form):
    username = StringField('用户名', [validators.Length(min=4, max=25),Myvalidators(message='用户名必须是张定')])
    email = StringField('邮箱地址', [validators.Length(min=6, max=35)])
    password = PasswordField('密码', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('确认密码')

