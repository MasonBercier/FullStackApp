"""empty message

Revision ID: bedfb9a9b30e
Revises: 9758552b7340
Create Date: 2023-03-12 23:25:09.114894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bedfb9a9b30e'
down_revision = '9758552b7340'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caught',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ability', sa.String(), nullable=True),
    sa.Column('base_exp', sa.Integer(), nullable=True),
    sa.Column('sprite_url', sa.String(), nullable=True),
    sa.Column('attack_stat', sa.Integer(), nullable=True),
    sa.Column('hp_stat', sa.Integer(), nullable=True),
    sa.Column('defense_stat', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('poketeam',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('caught_poke', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['caught_poke'], ['caught.name'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('poketeam')
    op.drop_table('caught')
    # ### end Alembic commands ###
