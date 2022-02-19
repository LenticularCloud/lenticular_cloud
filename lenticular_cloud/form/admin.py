from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, \
        TextAreaField, PasswordField, IntegerField, FloatField, \
        DateTimeField, DateField, FormField, BooleanField, \
        SelectField, Form as NoCsrfForm, SelectMultipleField

from wtforms.fields.html5 import URLField
from wtforms.fields import FormField

from .base import FieldList

class OAuth2ClientForm(FlaskForm):
    client_id = StringField(gettext('client_id') )
    client_name = StringField(gettext('client_name'))
    client_uri = URLField(gettext('client_uri'))
    client_secret = PasswordField(gettext('client_secret'))
    logo_uri = URLField(gettext('logo_uri'))
    redirect_uris = FieldList(FormField(URLField(gettext('logo_uri'))))
    #contacts = List[str]
    #grant_types = List[str]
    #response_types = List[str]
    scope = StringField(gettext('scope'))
    subject_type = StringField(gettext('subject_type'))
    token_endpoint_auth_method = StringField(gettext('token_endpoint_auth_method'))
    userinfo_signed_response_alg = StringField(gettext('userinfo_signed_response_alg'))

    client_secret_expires_at = IntegerField('client_secret_expires_at')


    #allowed_cross_origins = Array
    #audience = List[str]


    submit = SubmitField(gettext('Update'))
