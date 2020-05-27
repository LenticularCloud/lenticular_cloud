from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, \
        TextAreaField, PasswordField, IntegerField, FloatField, \
        DateTimeField, DateField, FormField, BooleanField, \
        SelectField, Form as NoCsrfForm, SelectMultipleField
from wtforms.fields.html5 import EmailField
from wtforms.widgets.html5 import NumberInput, DateInput
from wtforms.validators import DataRequired, NumberRange, Optional, NoneOf, Length
from datetime import datetime


class LoginForm(FlaskForm):
    name = StringField(gettext('Username'), validators=[DataRequired()])
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


class ConsentForm(FlaskForm):
#   scopes = SelectMultipleField(gettext('scopes'))
#   audiences = SelectMultipleField(gettext('audiences'))
    remember = BooleanField(gettext('remember me'))
    submit = SubmitField()


class RegistrationForm(FlaskForm):
    username = StringField(gettext('Username'), validators=[DataRequired()])
    password = PasswordField(gettext('Password'), validators=[DataRequired()])
    alternative_email = EmailField(gettext('Alternative Email'))
    submit = SubmitField()
