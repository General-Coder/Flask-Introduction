from .ext import db

class News(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    title = db.Column(
        db.String(30),
        index=True
    )
    content = db.Column(
        db.String(255),
        nullable=True
    )
    def model_to_dict(self):
        data = {
            'id':self.id,
            'title':self.title,
            'content':self.content
,        }
        return data