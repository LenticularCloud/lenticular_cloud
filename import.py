import logging
from lenticular_cloud.app import init_app
from lenticular_cloud.model import User

name = 'oidc_provider'
app = init_app(name)
logging.basicConfig(level=logging.DEBUG)

with app.app_context():
    for ldap_user in User.query_().all():
        user = User.query.filter_by(username=str(ldap_user.username)).first()
        print(user)

