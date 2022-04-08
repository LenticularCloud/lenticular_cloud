from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, \
        TextAreaField, PasswordField, IntegerField, FloatField, \
        DateTimeField, DateField, FormField, BooleanField, \
        SelectField, Form as NoCsrfForm, SelectMultipleField, \
        HiddenField
from wtforms.fields.html5 import EmailField
from wtforms.widgets.html5 import NumberInput, DateInput
from wtforms.validators import DataRequired, NumberRange, Optional, NoneOf, Length, Regexp, InputRequired
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


class WebauthnLoginForm(FlaskForm):
    """webauthn login form"""

    assertion = HiddenField('Assertion', [InputRequired()])

class Fido2Form(FlaskForm):
    fido2 = TextField(gettext('Fido2'), default="Javascript Required")
    submit = SubmitField(gettext('Authorize'))


class ConsentForm(FlaskForm):
#   scopes = SelectMultipleField(gettext('scopes'))
#   audiences = SelectMultipleField(gettext('audiences'))
    remember = BooleanField(gettext('remember'))
    submit = SubmitField()


class RegistrationForm(FlaskForm):
    username = StringField(gettext('Username'), validators=[
        DataRequired(),
        Regexp('^[a-zA-Z0-9-.]+$', message=gettext('Only `a-z`, `A-Z`, `0-9`, `-.` is allowed for username'))
        ])
    password = PasswordField(gettext('Password'), validators=[
        DataRequired(),
        Length(min=6)
        ])
    alternative_email = EmailField(gettext('Alternative Email'), render_kw={"placeholder": "Optional"})
    submit = SubmitField()
