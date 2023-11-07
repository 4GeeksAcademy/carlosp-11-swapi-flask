"""empty message

Revision ID: fd782effb21f
Revises: 58af5a4a48ed
Create Date: 2023-11-07 11:41:30.050233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd782effb21f'
down_revision = '58af5a4a48ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite_peoples', schema=None) as batch_op:
        batch_op.add_column(sa.Column('people_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('favorite_peoples_character_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'peoples', ['people_id'], ['id'])
        batch_op.drop_column('character_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite_peoples', schema=None) as batch_op:
        batch_op.add_column(sa.Column('character_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorite_peoples_character_id_fkey', 'peoples', ['character_id'], ['id'])
        batch_op.drop_column('people_id')

    # ### end Alembic commands ###