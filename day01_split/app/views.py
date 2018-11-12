from flask import Blueprint, url_for, redirect, render_template, request, make_response, abort, session

blue = Blueprint(
    name='split',
    import_name=__name__
)


@blue.route('/split/')
def split():
    return 'split'


@blue.route('/params/<string:id>/<int:num>/')
def params(id, num):
    print(id)
    print(type(id))
    return id


@blue.route('/params/<path:my_path>/')
def param_path(my_path):
    print(type(my_path))
    return my_path


@blue.route('/any/<any(a,ab,c,d):p>/')
def my_any(p):
    # print(p)
    # print(type(p))
    # res = url_for('split.split')
    res = url_for('split.params', id='haha', num=3)
    # return  redirect(res)
    return render_template('one.html')


@blue.route('/req/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def look_req():
    req = request
    print('method', req.method)
    print('path', req.path)
    print('url', req.url)
    print('args', req.args)
    print('form', req.form)
    print('base_url', req.base_url)
    print('name', req.args.getlist('name'))
    print('name', req.args.get('name'))
    print('form_name', req.form.get('name'))
    print('remote_addr', req.remote_addr)
    print('remote_user', req.remote_user)
    print('file', req.files)
    print('file_name', req.files.get('name'))
    print(dir(req))
    return 'ok'


@blue.route('/response/')
def my_response():
    # response = make_response('hehe')
    abort(403)
    return 'hehe', 404


@blue.errorhandler(403)
def handle_403(e):
    print(e)
    return '无权限'


@blue.route('/home/')
def home():
    # 通过cookies获取
    uname = request.cookies.get('name')
    session_name = session.get('uname')
    uname = uname if uname else '游客'
    session_name = session_name if session_name else  '游客1'
    return render_template('home.html',uname=uname,session_name=session_name)


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        # 解析post请求参数
        name = request.form.get('name')
        name1 = request.form.get('name1')

        #设置session
        session['uname'] = name1
        # 设置cookie
        response = redirect(url_for('split.home'))
        response.set_cookie('name', name, max_age=30)
        # 重定向到home页面
        return response
    else:
        abort(405)


@blue.route('/logout/')
def logout():
    response = redirect(url_for('split.home'))
    response.delete_cookie('name')
    session.pop('uname')
    return response
