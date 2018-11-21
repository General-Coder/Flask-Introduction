from flask_restful import reqparse


register_args = reqparse.RequestParser()
register_args.add_argument('email',required = True,help = 'email必填',location = 'form')
register_args.add_argument('pwd',required  = True,help = '密码必填',location = 'form')
register_args.add_argument('confirm_pwd',required  = True,help = '确认密码必填字段',location = 'form')

login_args = register_args.copy()
login_args.remove_argument('confirm_pwd')

delete_args = reqparse.RequestParser()
delete_args.add_argument('c_id',required=True,location='form')

change_args= reqparse.RequestParser()
change_args.add_argument('c_id',required=True,location='form')
change_args.add_argument('longname',location='form')
change_args.add_argument('fics',location='form')
change_args.add_argument('price',location='form')
change_args.add_argument('mprice',location='form')
change_args.add_argument('nums',location='form')

status_args = reqparse.RequestParser()
status_args.add_argument('o_id',type=int,location = 'form',required=True)
status_args.add_argument('status',type=int,location = 'form',required=True)
