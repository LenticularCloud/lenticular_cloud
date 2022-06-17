from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, \
        TextAreaField, PasswordField, IntegerField, FloatField, \
        DateTimeField, DateField, FormField, BooleanField, \
        SelectField, Form as NoCsrfForm, HiddenField
from wtforms.widgets import NumberInput, DateInput
from wtforms.validators import DataRequired, NumberRange, \
        Optional, NoneOf, Length, EqualTo, InputRequired


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
    token = StringField(gettext('totp-verify token'))
    name = StringField(gettext('name'))
    submit = SubmitField(gettext('Activate'))


class TOTPDeleteForm(FlaskForm):
    submit = SubmitField(gettext('Delete'))


class WebauthnRegisterForm(FlaskForm):
    """webauthn register token form"""

    attestation = HiddenField('Attestation', [InputRequired()])
    name = StringField('Name', [Length(max=250)])
    submit = SubmitField('Register', render_kw={'disabled': True})

class PasswordChangeForm(FlaskForm):
    password_old = PasswordField(gettext('Old Password'), validators=[DataRequired()])
    password_new = PasswordField(gettext('New Password'), validators=[DataRequired()])
    password_repeat = PasswordField(gettext('Repeat Password'), validators=[DataRequired(),EqualTo('password_new')])
    submit = SubmitField(gettext('Change Password'))

class OidcAuthenticationConfirm(FlaskForm):
    submit = SubmitField(gettext('Continue'))
