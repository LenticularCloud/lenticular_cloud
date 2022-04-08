from authlib.integrations.base_client.errors import MissingTokenError
from flask import Blueprint, redirect, request, url_for, render_template
from flask import current_app, session
from flask import jsonify
from flask.typing import ResponseReturnValue
from flask_login import current_user, logout_user
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from authlib.integrations.base_client.errors import InvalidTokenError
from ory_hydra_client.api.admin import list_o_auth_2_clients, get_o_auth_2_client, update_o_auth_2_client, create_o_auth_2_client 
from ory_hydra_client.models import OAuth2Client, GenericError
from typing import Optional
import logging

from ..model import db, User, UserSignUp
from .oauth2 import redirect_login, oauth2
from ..form.admin import OAuth2ClientForm
from ..hydra import hydra_service


admin_views = Blueprint('admin', __name__, url_prefix='/admin')
logger = logging.getLogger(__name__)


def before_request() -> Optional[ResponseReturnValue]:
    try:
        resp = oauth2.custom.get('/userinfo')
        data = resp.json()
        if not current_user.is_authenticated or resp.status_code != 200:
            return redirect_login()
        if 'groups' not in data or 'admin' not in data['groups']:
            return 'Not an admin', 403
    except (MissingTokenError, InvalidTokenError):
        return redirect_login()
    return None


admin_views.before_request(before_request)


@admin_views.route('/', methods=['GET', 'POST'])
async def index() -> ResponseReturnValue:
    return render_template('admin/index.html.j2')


@admin_views.route('/user', methods=['GET'])
async def users():
    users = User.query.all()
    return render_template('admin/users.html.j2', users=users)


@admin_views.route('/registrations', methods=['GET'])
def registrations() -> ResponseReturnValue:
    users = UserSignUp.query.all()
    return render_template('admin/registrations.html.j2', users=users)


@admin_views.route('/registration/<registration_id>', methods=['DELETE'])
def registration_delete(registration_id) -> ResponseReturnValue:
    user_data = UserSignUp.query.get(registration_id)
    if user_data is None:
        return jsonify({}), 404
    db.session.delete(user_data)
    db.session.commit()
    return jsonify({})


@admin_views.route('/registration/<registration_id>', methods=['PUT'])
def registration_accept(registration_id) -> ResponseReturnValue:
    user_data = UserSignUp.query.get(registration_id)
    #create user
    user = User.new(user_data)

    db.session.add(user)
    db.session.delete(user_data)
    db.session.commit()
    return jsonify({})


@admin_views.route('/clients')
async def clients() -> ResponseReturnValue:
    clients = await list_o_auth_2_clients.asyncio(_client=hydra_service.hydra_client)
    return render_template('admin/clients.html.j2', clients=clients)

@admin_views.route('/client/<client_id>', methods=['GET', 'POST'])
async def client(client_id: str) -> ResponseReturnValue:
    
    client = await get_o_auth_2_client.asyncio(client_id, _client=hydra_service.hydra_client)
    if client is None or isinstance( client, GenericError):
        logger.error(f"oauth2 client not found with id: '{client_id}'")
        return 'client not found', 404

    form = OAuth2ClientForm(obj=client)
    if form.validate_on_submit():
        form.populate_obj(client)
 
        client = await update_o_auth_2_client.asyncio(id=client_id ,json_body=client, _client=hydra_service.hydra_client)
        if client is None or isinstance(client, GenericError):
            logger.error(f"oauth2 client update failed: '{client_id}'")
            return 'client update failed', 500


        
    return render_template('admin/client.html.j2', client=client, form=form)


@admin_views.route('/client_new', methods=['GET','POST'])
async def client_new() -> ResponseReturnValue:
    
    client = OAuth2Client()

    form = OAuth2ClientForm()
    if form.validate_on_submit():
        form.populate_obj(client)
 
        resp_client = await create_o_auth_2_client.asyncio(json_body=client, _client=hydra_service.hydra_client)
        if resp_client is None:
            logger.error(f"oauth2 client update failed: '{client.client_id}'")
            return 'internal error', 500
        return redirect(url_for('.client', client_id=client.client_id))


    return render_template('admin/client.html.j2', client=client, form=form)
