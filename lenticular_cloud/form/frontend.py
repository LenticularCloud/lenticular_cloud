from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, \
        TextAreaField, PasswordField, IntegerField, FloatField, \
        DateTimeField, DateField, FormField, BooleanField, \
        SelectField, Form as NoCsrfForm
from wtforms.widgets.html5 import NumberInput, DateInput
from wtforms.validators import DataRequired, NumberRange, Optional, NoneOf, Length
from datetime import datetime



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
