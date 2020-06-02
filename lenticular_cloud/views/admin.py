import flask
from flask import Blueprint, redirect, request, url_for, render_template
from flask import current_app, session
from flask import jsonify
from flask_login import current_user, logout_user
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from ..model import db, User, UserSignUp
from .frontend import redirect_login


admin_views = Blueprint('admin', __name__, url_prefix='/admin')


def before_request():
    try:
        resp = current_app.oauth.session.get('/userinfo')
        data = resp.json()
        if not current_user.is_authenticated or resp.status_code is not 200:
            return redirect_login()
        if 'admin' not in data['groups']:
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
