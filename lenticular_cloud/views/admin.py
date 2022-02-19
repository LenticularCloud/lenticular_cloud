import flask
from flask import Blueprint, redirect, request, url_for, render_template
from flask import current_app, session
from flask import jsonify
from flask_login import current_user, logout_user
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
import ory_hydra_client
from ory_hydra_client.model.o_auth2_client import OAuth2Client
import logging

from ..model import db, User, UserSignUp
from .frontend import redirect_login
from ..form.admin import OAuth2ClientForm


admin_views = Blueprint('admin', __name__, url_prefix='/admin')
logger = logging.getLogger(__name__)


def before_request():
    try:
        resp = current_app.oauth.session.get('/userinfo')
        data = resp.json()
        if not current_user.is_authenticated or resp.status_code != 200:
            return redirect_login()
        if 'groups' not in data or 'admin' not in data['groups']:
            return 'Not an admin', 403
    except TokenExpiredError:
        return redirect_login()


admin_views.before_request(before_request)


@admin_views.route('/', methods=['GET', 'POST'])
def index():
    return render_template('admin/index.html.j2')


@admin_views.route('/user', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('admin/users.html.j2', users=users)


@admin_views.route('/registrations', methods=['GET'])
def registrations():
    users = UserSignUp.query.all()
    return render_template('admin/registrations.html.j2', users=users)


@admin_views.route('/registration/<registration_id>', methods=['DELETE'])
def registration_delete(registration_id):
    user_data = UserSignUp.query.get(registration_id)
    if user_data is None:
        return jsonify({}), 404
    db.session.delete(user_data)
    db.session.commit()
    return jsonify({})


@admin_views.route('/registration/<registration_id>', methods=['PUT'])
def registration_accept(registration_id):
    user_data = UserSignUp.query.get(registration_id)
    #create user
    user = User.new(user_data)

    db.session.add(user)
    db.session.delete(user_data)
    db.session.commit()
    return jsonify({})


@admin_views.route('/clients')
def clients():
    clients = current_app.hydra_api.list_o_auth2_clients()
    return render_template('admin/clients.html.j2', clients=clients)

@admin_views.route('/client/<client_id>', methods=['GET', 'POST'])
def client(client_id: str):
    
    try:
        client = current_app.hydra_api.get_o_auth2_client(client_id)
    except ory_hydra_client.ApiException as e:
        logger.error(f"oauth2 client not found with id: '{client_id}'")
        return 'client not found', 404

    form = OAuth2ClientForm(obj=client)
    if form.validate_on_submit():
        form.populate_obj(client)
 
        try:
            client = current_app.hydra_api.update_o_auth2_client(client_id, client)
        except ory_hydra_client.ApiException as e:
            logger.error(f"oauth2 client update failed: '{client_id}'")
            return 'client update failed', 500


        
    return render_template('admin/client.html.j2', client=client, form=form)


@admin_views.route('/client_new', methods=['GET','POST'])
def client_new():
    
    client = OAuth2Client()

    form = OAuth2ClientForm()
    if form.validate_on_submit():
        form.populate_obj(client)
 
        try:
            client = current_app.hydra_api.create_o_auth2_client(client)
        except ory_hydra_client.ApiException as e:
            logger.error(f"oauth2 client update failed: '{client.client_id}'")
            return 'internal error', 500
        return redirect(url_for('.client', client_id=client.client_id))


    return render_template('admin/client.html.j2', client=client, form=form)
