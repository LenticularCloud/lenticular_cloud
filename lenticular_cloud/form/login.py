from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, \
        TextAreaField, PasswordField, IntegerField, FloatField, \
        DateTimeField, DateField, FormField, BooleanField, \
        SelectField, Form as NoCsrfForm
from wtforms.widgets.html5 import NumberInput, DateInput
from wtforms.validators import DataRequired, NumberRange, Optional, NoneOf, Length
from datetime import datetime


class LoginForm(FlaskForm):
    name = StringField(gettext('User Name'), validators=[DataRequired()])
    submit = SubmitField(gettext('Login'))


class PasswordForm(FlaskForm):
    password = PasswordField(gettext('Password'))
    submit = SubmitField(gettext('Authorize'))


class TotpForm(FlaskForm):
    totp = TextField(gettext('2FA Token'))
    submit = SubmitField(gettext('Authorize'))


class Fido2Form(FlaskForm):
    fido2 = TextField(gettext('Fido2'), default="Javascript Required")
    submit = SubmitField(gettext('Authorize'))
