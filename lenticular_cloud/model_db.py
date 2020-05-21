from flask_sqlalchemy import SQLAlchemy, orm
import uuid

db = SQLAlchemy()  # type: SQLAlchemy


def generate_uuid():
    return str(uuid.uuid4())


class OAuth(db.Model):
    token = db.Column(db.Text, primary_key=True)
    provider = db.Column(db.Text)
    provider_username = db.Column(db.Text)


class User(db.Model):
    id = db.Column(db.String(length=36), primary_key=True, default=generate_uuid)
    username = db.Column(db.String, unique=True)


class Client(db.Model):
    key = db.Column(db.Text, primary_key=True)
    value = db.Column(db.Text)


class AuthzCode(db.Model):
    key = db.Column(db.Text, primary_key=True)
    value = db.Column(db.Text)


class AccessToken(db.Model):
    key = db.Column(db.Text, primary_key=True)
    value = db.Column(db.Text)


class RefreshToken(db.Model):
    key = db.Column(db.Text, primary_key=True)
    value = db.Column(db.Text)


class SubjectIdentifier(db.Model):
    key = db.Column(db.Text, primary_key=True)
    value = db.Column(db.Text)


