from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, \
        TextAreaField, PasswordField, IntegerField, FloatField, \
        DateTimeField, DateField, FormField, BooleanField, \
        SelectField, Form as NoCsrfForm, SelectMultipleField

from wtforms.fields import URLField
from wtforms.fields import FormField, SelectMultipleField

from .base import FieldList

class SerilizedSelectField(SelectMultipleField):

    def process_data(self, value):
        try:
            self.data = ','.join(list(self.coerce(v) for v in value))
        except (ValueError, TypeError):
            self.data = None

    def process_formdata(self, valuelist):
        try:
            self.data = ','.join(list(self.coerce(x) for x in valuelist))
        except ValueError as exc:
            raise ValueError(
                self.gettext(
                    "Invalid choice(s): one or more data inputs could not be coerced."
                )
            ) from exc

    def populate_obj(self, obj, name) -> None:
        setattr(obj, name, ','.join(self.data))



class OAuth2ClientForm(FlaskForm):
    client_id = StringField(gettext('client_id') )
    client_name = StringField(gettext('client_name'))
    client_uri = URLField(gettext('client_uri'))
    token_endpoint_auth_method =  SelectField('token_endpoint_auth_method', choices=[(x, x) for x in ['client_secret_basic', 'client_secret_post', 'private_key_jwt', 'none']])
    client_secret = PasswordField(gettext('client_secret'))
    logo_uri = URLField(gettext('logo_uri'))
    redirect_uris = FieldList(URLField(gettext('redirect_uri')), min_entries=1)
    contacts =   FieldList(StringField('contacts'))
    grant_types =  SelectMultipleField('grant_types',choices=[(x, x) for x in ['authorization_code', 'refresh_token', 'implicit', 'urn:ietf:params:oauth:grant-type:jwt-bearer']])
    response_types = SelectMultipleField('repsonse_type',choices=[(x, x) for x in ['code', 'token', 'id_token']])
    scope = StringField(gettext('scope'))
    subject_type = StringField(gettext('subject_type'))
    userinfo_signed_response_alg = SelectField(gettext('userinfo_signed_response_alg'), choices=[(x, x) for x in ['none', 'RS256']])
    allowed_cors_origins = FieldList(StringField('allowed_cors_origins'))

    client_secret_expires_at = IntegerField('client_secret_expires_at')


    #allowed_cross_origins = Array
    contacts =   FieldList(StringField('contacts'))
    #audience = List[str]


    submit = SubmitField(gettext('Update'))
