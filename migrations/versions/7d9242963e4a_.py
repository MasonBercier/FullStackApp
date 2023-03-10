"""empty message

Revision ID: 7d9242963e4a
Revises: 5633f72e2d5a
Create Date: 2023-03-09 12:17:55.821475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d9242963e4a'
down_revision = '5633f72e2d5a'
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
