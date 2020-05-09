from flask_sqlalchemy import SQLAlchemy, orm

db = SQLAlchemy()  # type: SQLAlchemy


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


