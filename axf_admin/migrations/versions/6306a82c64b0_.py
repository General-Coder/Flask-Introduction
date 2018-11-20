"""empty message

Revision ID: 6306a82c64b0
Revises: e8d66fca2b4f
Create Date: 2018-11-20 09:52:44.568164

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6306a82c64b0'
down_revision = 'e8d66fca2b4f'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('is_delete', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_delete')
    op.drop_column('user', 'is_active')