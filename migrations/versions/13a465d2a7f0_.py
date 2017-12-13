"""empty message

Revision ID: 13a465d2a7f0
Revises: None
Create Date: 2017-12-12 21:43:10.936992

"""

# revision identifiers, used by Alembic.
revision = '13a465d2a7f0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teams')
    # ### end Alembic commands ###
