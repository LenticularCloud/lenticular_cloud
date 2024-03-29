"""remove ldap, add rest to db

Revision ID: 0518a8625b50
Revises: 52a21983d2a8
Create Date: 2022-06-17 13:15:33.450531

"""
from alembic import op
import sqlalchemy as sa
from flask import current_app
from lenticular_cloud.model import User
import logging


# revision identifiers, used by Alembic.
revision = '0518a8625b50'
down_revision = '52a21983d2a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_name', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('user_sign_up')
    op.add_column('user', sa.Column('password_hashed', sa.String(), server_default="", nullable=False))
    op.add_column('user', sa.Column('enabled', sa.Boolean(), server_default="false", nullable=True))
    # ### end Alembic commands ###
    try:
        from ldap3_orm import AttrDef, EntryBase as _EntryBase, ObjectDef, EntryType
        from ldap3_orm import Reader
        from ldap3 import Connection, Server, ALL

        app = current_app
        server = Server(app.config['LDAP_URL'], get_info=ALL)
        ldap_conn = Connection(server, app.config['LDAP_BIND_DN'], app.config['LDAP_BIND_PW'], auto_bind=True) # TODO auto_bind read docu
        base_dn = app.config['LDAP_BASE_DN']
        object_def = ObjectDef(["inetOrgPerson"], ldap_conn)
        user_base_dn = f"ou=users,{base_dn}"



        op.execute(User.__table__.update().values({'enabled': True}))
        conn = op.get_bind()
        users = conn.execute(User.__table__.select())

        for user in users:
            print(f"migrating user {user.username}")
            reader = Reader(ldap_conn, object_def, user_base_dn, f'(uid={user.username})')
            result = reader.search()
            if len(result) == 0:
                print(f"WARNING: could not migrate user {user.username}")
                continue
            ldap_object = result[0]
            password_hashed = ldap_object.userPassword[0].decode().replace('{CRYPT}','')
            op.execute(User.__table__.update().values({'password_hashed': password_hashed}).where(User.id == user.id))
    except ModuleNotFoundError:
        print("ignore import warning")



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'enabled')
    op.drop_column('user', 'password_hashed')
    op.create_table('user_sign_up',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('password', sa.VARCHAR(), nullable=False),
    sa.Column('alternative_email', sa.VARCHAR(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('group')
    op.drop_table('app_token')
    # ### end Alembic commands ###
