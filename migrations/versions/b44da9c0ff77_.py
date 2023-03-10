"""empty message

Revision ID: b44da9c0ff77
Revises: 09f0b2db51f9
Create Date: 2023-03-07 21:40:50.109190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b44da9c0ff77'
down_revision = '09f0b2db51f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('poke_team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('poke_team')
    # ### end Alembic commands ###
