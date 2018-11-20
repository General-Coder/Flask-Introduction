from datetime import datetime

from .ext import db


# 会员
class User(db.Model):
    __tablename__ = 'user'
    # 编号
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    # 昵称
    name = db.Column(
        db.String(100),
        unique=True
    )
    # 密码
    pwd = db.Column(
        db.String(100)
    )
    # 邮箱
    email = db.Column(
        db.String(100),
        unique=True
    )
    # 手机
    phone = db.Column(
        db.String(11),
        unique=True
    )
    # 个人简介
    info = db.Column(
        db.TEXT
    )
    # 头像
    face = db.Column(
        db.String(255)
    )
    # 时间
    addtime = db.Column(
        db.DateTime,
        index=True,
        default=datetime.now
    )
    # 唯一标识符
    uuid = db.Column(
        db.String(255),
        unique=True
    )
    userlogs = db.relationship(
        'UserLog',
        backref='user'
    )
    comments = db.relationship(
        'Comment',
        backref='user'
    )
    moviecols = db.relationship(
        'Moviecol',
        backref='user'
    )

    def __repr__(self):
        return '<User %r>' % self.name


# 会员登陆日志
class UserLog(db.Model):
    __tablename__ = 'userlog'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )
    ip = db.Column(
        db.String(100)
    )
    addtime = db.Column(
        db.DateTime,
        index=True,
        default=datetime.now
    )

    def __repr__(self):
        return '<Userlog %r>' % self.id


# 标签
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, default=datetime.now)
    movies = db.relationship('Movie', backref='tag')

    def __repr__(self):
        return '<Tag %r>' % self.name


# 电影
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 地址
    info = db.Column(db.Text)  # 简介
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 播放时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    comments = db.relationship('Comment', backref='movie')
    moviecols = db.relationship('Moviecol', backref='movie')

    def __repr__(self):
        return '<Movie %r>' % self.title


# 上映预告
class Preview(db.Model):
    __tablename__ = 'Preview'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    logo = db.Column(db.String(255), unique=True)  # 封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return '<Preview %r>' % self.title


# 评论
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 内容
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return '<Comment %r>' % self.id


# 电影收藏
class Moviecol(db.Model):
    __tablename__ = 'moviecol'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return '<Moviecol %r>' % self.id


# 权限
class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(255), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return '<Auth %r>' % self.name


# 角色
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(255), unique=True)  # 名称
    auths = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    admins = db.relationship('Admin', backref='role')  # 管理员外键关联

    def __repr__(self):
        return '<Role %r>' % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = 'admin'
    # 编号
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    # 管理员账号
    name = db.Column(
        db.String(100),
        unique=True
    )
    # 密码
    pwd = db.Column(
        db.String(100)
    )
    # 是否为超级管理员，0为超级管理员
    is_super = db.Column(
        db.SmallInteger
    )
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 所属角色
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    adminlogs = db.relationship('AdminLog', backref='admin')
    oplogs = db.relationship('OpLog', backref='admin')

    def __repr__(self):
        return '<Admin %r>' % self.name


# 登录日志
class AdminLog(db.Model):
    __tablename__ = 'adminlog'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    admin_id = db.Column(
        db.Integer,
        db.ForeignKey('admin.id')
    )
    ip = db.Column(
        db.String(100)
    )
    addtime = db.Column(
        db.DateTime,
        index=True,
        default=datetime.now
    )

    def __repr__(self):
        return '<Adminlog %r>' % self.id


# 操作日志
class OpLog(db.Model):
    __tablename__ = 'oplog'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    admin_id = db.Column(
        db.Integer,
        db.ForeignKey('admin.id')
    )
    ip = db.Column(
        db.String(100)
    )
    # 操作原因
    reason = db.Column(
        db.String(600)
    )
    addtime = db.Column(
        db.DateTime,
        index=True,
        default=datetime.now
    )

    def __repr__(self):
        return '<OpLog %r>' % self.id
