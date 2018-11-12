from flask import Blueprint

#实例化蓝图
blue = Blueprint(
    name='hello',
    import_name=__name__
)

@blue.route('/blue/')
def hell_blue_print():
    return '我是蓝图,规划URL'