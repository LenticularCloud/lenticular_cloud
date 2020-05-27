from flask_sqlalchemy import SQLAlchemy, orm
from datetime import datetime
import uuid
import pyotp

db = SQLAlchemy()  # type: SQLAlchemy


def generate_uuid():
    return str(uuid.uuid4())


class User(db.Model):
    id = db.Column(
            db.String(length=36), primary_key=True, default=generate_uuid)
    username = db.Column(
            db.String, unique=True)

    totps = db.relationship('Totp', back_populates='user')


class Totp(object):
    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    user_id = db.Column(
            db.Integer,
            db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)

    def verify(self, token: str):
        totp = pyotp.TOTP(self._secret)
        return totp.verify(token)
