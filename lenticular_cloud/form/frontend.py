from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, \
        TextAreaField, PasswordField, IntegerField, FloatField, \
        DateTimeField, DateField, FormField, BooleanField, \
        SelectField, Form as NoCsrfForm, HiddenField
from wtforms.widgets.html5 import NumberInput, DateInput
from wtforms.validators import DataRequired, NumberRange, \
        Optional, NoneOf, Length


class ClientCertForm(FlaskForm):
    publickey = TextAreaField(gettext('Public Key'), validators=[
            DataRequired()
        ])
    valid_time = IntegerField(
            gettext('valid time in days'),
            default=365,
            validators=[
                DataRequired(),
                NumberRange(min=1, max=365*2)
            ])
    submit = SubmitField(gettext('Submit'))


class TOTPForm(FlaskForm):
    secret = HiddenField(gettext('totp-Secret'))
    token = TextField(gettext('totp-verify token'))
    name = TextField(gettext('name'))
    submit = SubmitField(gettext('Activate'))


class TOTPDeleteForm(FlaskForm):
    submit = SubmitField(gettext('Delete'))


class OidcAuthenticationConfirm(FlaskForm):
    submit = SubmitField(gettext('Continue'))
