"""empty message

Revision ID: 156fb1791c8e
Revises: 1f0e88abce96
Create Date: 2021-11-06 16:40:02.568356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '156fb1791c8e'
down_revision = '1f0e88abce96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
