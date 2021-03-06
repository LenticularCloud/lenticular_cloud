from urllib.parse import urlencode, parse_qs

import flask
from flask import Blueprint, redirect, request
from flask import current_app, session
from flask import jsonify
from flask.helpers import make_response
from flask.templating import render_template
from oic.oic.message import TokenErrorResponse, UserInfoErrorResponse, EndSessionRequest
from flask_login import current_user, login_required

from pyop.access_token import AccessToken, BearerTokenError
from pyop.exceptions import InvalidAuthenticationRequest, InvalidAccessToken, InvalidClientAuthentication, OAuthError, \
    InvalidSubjectIdentifier, InvalidClientRegistrationRequest
from pyop.util import should_fragment_encode

from ..form.frontend import OidcAuthenticationConfirm

oidc_provider_views = Blueprint('oidc_provider', __name__, url_prefix='')


@oidc_provider_views.route('/registration', methods=['POST'])
def registration_endpoint():
    try:
        response = current_app.provider.handle_client_registration_request(flask.request.get_data().decode('utf-8'))
        return make_response(jsonify(response.to_dict()), 201)
    except InvalidClientRegistrationRequest as e:
        print(e)
        return make_response(jsonify(str(e)), 400)


@oidc_provider_views.route('/authentication', methods=['GET'])
@login_required
def authentication_endpoint_confirm():
    form = OidcAuthenticationConfirm()
    auth_req = current_app.provider.parse_authentication_request(urlencode(flask.request.args),
                                                                     flask.request.args)
    return render_template('frontend/oidc_authentication.html.j2', form=form, auth_req=auth_req)


@oidc_provider_views.route('/authentication', methods=['POST'])
@login_required
def authentication_endpoint():
    # parse authentication request
    print(request)
    print(request.headers)
    try:
        auth_req = current_app.provider.parse_authentication_request(urlencode(flask.request.args),
                                                                     flask.request.args)
    except InvalidAuthenticationRequest as e:
        current_app.logger.debug('received invalid authn request', exc_info=True)
        error_url = e.to_error_url()
        if error_url:
            return redirect(error_url, 303)
        else:
            # show error to user
            return make_response('Something went wrong: {}'.format(str(e)), 400)

    # automatically authentication
    authn_response = current_app.provider.authorize(auth_req, str(current_user.username))
    response_url = authn_response.request(auth_req['redirect_uri'], should_fragment_encode(auth_req))
    return redirect(response_url, 303)


@oidc_provider_views.route('/.well-known/openid-configuration')
def provider_configuration():
    return jsonify(current_app.provider.provider_configuration.to_dict())


@oidc_provider_views.route('/jwks')
def jwks_uri():
    return jsonify(current_app.provider.jwks)


@oidc_provider_views.route('/token', methods=['POST'])
def token_endpoint():
    try:
        token_response = current_app.provider.handle_token_request(flask.request.get_data().decode('utf-8'),
                                                                   flask.request.headers)
        return jsonify(token_response.to_dict())
    except InvalidClientAuthentication as e:
        current_app.logger.debug('invalid client authentication at token endpoint', exc_info=True)
        error_resp = TokenErrorResponse(error='invalid_client', error_description=str(e))
        response = make_response(error_resp.to_json(), 401)
        response.headers['Content-Type'] = 'application/json'
        response.headers['WWW-Authenticate'] = 'Basic'
        return response
    except OAuthError as e:
        current_app.logger.debug('invalid request: %s', str(e), exc_info=True)
        error_resp = TokenErrorResponse(error=e.oauth_error, error_description=str(e))
        response = make_response(error_resp.to_json(), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


@oidc_provider_views.route('/userinfo', methods=['GET', 'POST'])
def userinfo_endpoint():
    try:
        response = current_app.provider.handle_userinfo_request(flask.request.get_data().decode('utf-8'),
                                                                flask.request.headers)
        return jsonify(response.to_dict())
    except (BearerTokenError, InvalidAccessToken) as e:
        error_resp = UserInfoErrorResponse(error='invalid_token', error_description=str(e))
        response = make_response(error_resp.to_json(), 401)
        response.headers['WWW-Authenticate'] = AccessToken.BEARER_TOKEN_TYPE
        response.headers['Content-Type'] = 'application/json'
        return response


def do_logout():

    end_session_request = EndSessionRequest().deserialize(urlencode(flask.request.args)).to_dict()
    try:
        current_app.provider.logout_user(end_session_request=end_session_request)
    except InvalidSubjectIdentifier as e:
        return make_response('Logout unsuccessful!', 400)

    redirect_url = current_app.provider.do_post_logout_redirect(end_session_request)
    if redirect_url:
        return redirect(redirect_url, 303)

    return make_response('Logout successful!')


