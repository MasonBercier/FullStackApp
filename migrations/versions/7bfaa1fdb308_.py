"""empty message

Revision ID: 7bfaa1fdb308
Revises: 9935429351e7
Create Date: 2023-03-09 12:39:37.196687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bfaa1fdb308'
down_revision = '9935429351e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('caught', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poketeam_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'poketeam', ['poketeam_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poketeam_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'poketeam', ['poketeam_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('poketeam_id')

    with op.batch_alter_table('caught', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('poketeam_id')

    # ### end Alembic commands ###
