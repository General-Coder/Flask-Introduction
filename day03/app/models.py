from .ext import db


class Dog(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(30),
        nullable=True,
        unique=True
    )
    place = db.Column(
        db.String(50),
        default='九堡户口'
    )

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'place': self.place
        }
        return data


class Grade(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20),
        unique=True
    )
    stus = db.relationship(
        'Stu',
        backref='grades',
        lazy=True
    )


class Stu(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20),
        unique=True
    )
    grade = db.Column(
        db.Integer,
        db.ForeignKey('grade.id')
    )


class Xin(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(10),
        unique=True
    )
    phones = db.relationship(
        'Phone',
        backref = 'u',
        lazy = True
    )


class Phone(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(10),
        unique=True
    )
    u_id = db.Column(
        db.Integer,
        db.ForeignKey('xin.id')
    )


class Tag(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    title = db.Column(
        db.String(20),
        unique=True
    )


tags = db.Table(
    'tags',
    db.Column(
        'tag_id',
        db.Integer,
        db.ForeignKey(
            'tag.id'),
            primary_key=True

    ),
    db.Column(
        'book_id',
        db.Integer,
        db.ForeignKey(
            'book.id'),
            primary_key=True

    )
)


class Book(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20),
        unique=True
    )
    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('books', lazy=True),
        lazy=True
    )



