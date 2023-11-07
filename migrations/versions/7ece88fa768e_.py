"""empty message

Revision ID: 7ece88fa768e
Revises: 8ad5fdbade4b
Create Date: 2023-10-14 07:48:55.417428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ece88fa768e'
down_revision = '8ad5fdbade4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('birth_date', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('skin_color', sa.String(length=20), nullable=True),
    sa.Column('eyes_color', sa.String(length=20), nullable=True),
    sa.Column('hair_color', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('characters')
    # ### end Alembic commands ###
