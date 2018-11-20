from flask_restful import reqparse

my_params = reqparse.RequestParser()
my_params.add_argument('name')
my_params.add_argument('id',type=int,required = True,help='id是必填字段')
my_params.add_argument('hobby',required=True,action = 'append')


two_args = reqparse.RequestParser()
two_args.add_argument('name',location = ['form','args'])


three_args = my_params.copy()
three_args.replace_argument('id',help='我是新的')
three_args.remove_argument('hobby') #移除hobby
three_args.remove_argument('name') #移除name
three_args.add_argument('age',required=True,type=int)


login_args = reqparse.RequestParser()
login_args.add_argument('name',required = True,location = 'form')
login_args.add_argument('pwd',required = True,location = 'form')
login_args.add_argument('pwd1',required = True,location = 'form')