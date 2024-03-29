"""init

Revision ID: a74320a5d7a1
Revises: 
Create Date: 2023-10-01 20:15:53.795636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a74320a5d7a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hashed', sa.String(), nullable=False),
    sa.Column('alternative_email', sa.String(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('app_token',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('scopes', sa.String(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('last_used', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('webauthn_credential')
    op.drop_table('totp')
    op.drop_table('app_token')
    op.drop_table('user')
    op.drop_table('group')
    # ### end Alembic commands ###
