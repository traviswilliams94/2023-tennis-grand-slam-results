"""seeded data

Revision ID: 18233a81d288
Revises: 10a23bb69a7c
Create Date: 2023-07-17 16:53:59.263692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18233a81d288'
down_revision = '10a23bb69a7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('results', 'player_name')
    op.drop_column('results', 'tournament_name')
    op.add_column('tournaments', sa.Column('tournament_name', sa.String(), nullable=True))
    op.drop_column('tournaments', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournaments', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_column('tournaments', 'tournament_name')
    op.add_column('results', sa.Column('tournament_name', sa.VARCHAR(), nullable=True))
    op.add_column('results', sa.Column('player_name', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###