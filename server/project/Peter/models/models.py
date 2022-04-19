from datetime import datetime
from email.policy import default
from turtle import update
from unicodedata import name
from Peter.database import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<User if={id} name{name}>'.format(
            id=self.id, name=self.name
        )
