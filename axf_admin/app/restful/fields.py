from flask_restful import fields

public_fileds = {
    'code':fields.Integer(default=1),
    'msg':fields.String(default='ok'),
    'data':fields.String()
}