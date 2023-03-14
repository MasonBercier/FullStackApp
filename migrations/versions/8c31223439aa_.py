"""empty message

Revision ID: 8c31223439aa
Revises: e4857b78509c
Create Date: 2023-03-14 15:08:44.076978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c31223439aa'
down_revision = 'e4857b78509c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caught',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ability', sa.String(), nullable=True),
    sa.Column('base_exp', sa.Integer(), nullable=True),
    sa.Column('sprite_url', sa.String(), nullable=True),
    sa.Column('gif_sprite_url', sa.String(), nullable=True),
    sa.Column('attack_stat', sa.Integer(), nullable=True),
    sa.Column('hp_stat', sa.Integer(), nullable=True),
    sa.Column('defense_stat', sa.Integer(), nullable=True),
    sa.Column('primary_type', sa.String(), nullable=True),
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
