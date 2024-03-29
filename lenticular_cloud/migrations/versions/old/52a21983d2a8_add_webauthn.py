"""add webauthn

Revision ID: 52a21983d2a8
Revises: ff2f2e871dfc
Create Date: 2022-02-20 17:00:04.531393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52a21983d2a8'
down_revision = 'ff2f2e871dfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('webauthn_credential',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('user_handle', sa.String(length=64), nullable=False),
    sa.Column('credential_data', sa.LargeBinary(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('registered', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('webauthn_credential')
    # ### end Alembic commands ###
