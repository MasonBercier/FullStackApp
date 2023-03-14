"""empty message

Revision ID: e810eae34b84
Revises: 6257a53d33f4
Create Date: 2023-03-13 15:54:05.708207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e810eae34b84'
down_revision = '6257a53d33f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caught',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ability', sa.String(), nullable=True),
    sa.Column('base_exp', sa.Integer(), nullable=True),
    sa.Column('sprite_url', sa.String(), nullable=True),
    sa.Column('attack_stat', sa.Integer(), nullable=True),
    sa.Column('hp_stat', sa.Integer(), nullable=True),
    sa.Column('defense_stat', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('poketeam',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('caught_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['caught_name'], ['caught.name'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('poketeam')
    op.drop_table('caught')
    # ### end Alembic commands ###