from  flask_restful import fields

one_fields = {
    'id':fields.Integer,
    # 'title':fields.String
    'name':fields.String(attribute='title')
}

two_fields = {
    'name':fields.String(default='tom'),
    #列表里是字符串
    'hobby':fields.List(fields.String)
}

three_fileds = {
    'code':fields.Integer(default=1),
    'msg':fields.String(default='ok'),
    'data':fields.Nested(one_fields)
}

# four_fields = {
#     'code': fields.Integer(default=1),
#     'msg': fields.String(default='ok'),
#     'data': fields.List(fields.Nested(one_fields))
# }

four_fields = three_fileds
four_fields['data'] = fields.List(fields.Nested(one_fields))

login_fileds = {
    'code':fields.Integer(default=1),
    'msg':fields.String(default='ok')
}