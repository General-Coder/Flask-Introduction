from .ext import db
from .util import enc_pwd


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(30), unique=True, index=True)
    pwd = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean,default=False)
    is_delete = db.Column(db.Boolean,default=False)

    @classmethod
    def create_user(cls,email, pwd,name=None):
        # email能否搜到一个用户,检查email
        users = User.query.filter(User.email == email).first()
        if users:
            # raise Exception('该email已被使用')
            return None
        # 加密密码
        user_pwd = enc_pwd(pwd)
        # 创建用户
        name = name if name else email
        user = cls(name=name, pwd=user_pwd, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    #重置密码
    def set_pwd(self, pwd):
        if not pwd or len(pwd) == 0:
            raise Exception('密码不能为空')
        self.pwd = enc_pwd(pwd)
        db.session.add(self)
        db.session.commit()
        return True

    #检测密码
    def check_pwd(self,pwd):
        u_pwd = enc_pwd(pwd)
        if u_pwd == self.pwd:
            return True
        else:
            return  False

class Goods(db.Model):
    __tablename__ = 'axf_goods'
    id = db.Column(
        db.Integer,
        autoincrement=True,
        primary_key=True
    )
    productid = db.Column(
        db.String(20)
    )
    productimg = db.Column(
        db.String(255)
    )
    productname = db.Column(
        db.String(130)
    )
    productlongname = db.Column(
        db.String(190)
    )
    isxf = db.Column(
        db.Boolean(),
        default=False
    )
    pmdesc = db.Column(
        db.Integer
    )
    specifics = db.Column(
        db.String(40)
    )
    price = db.Column(
        db.Numeric(precision=10, scale=2)
    )
    marketprice = db.Column(
        db.Numeric(precision=10, scale=2)
    )
    categoryid = db.Column(
        db.Integer
    )
    childcid = db.Column(db.Integer)
    childcidname = db.Column(
        db.String(30)
    )
    dealerid = db.Column(
        db.String(30)
    )
    storenums = db.Column(
        db.Integer
    )
    productnum = db.Column(
        db.Integer
    )
    is_delete = db.Column(
        db.Boolean,
        default=False
    )


