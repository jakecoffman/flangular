import json
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    username = db.Column(db.String(128), primary_key=True)
    email = db.Column(db.String(64))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

    def __str__(self):
        return json.dumps({
            'username': self.username,
            'email': self.email
        })
