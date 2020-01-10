"""Added Date on Update

Revision ID: b8de193c2477
Revises: 9b02a1331612
Create Date: 2020-01-10 14:01:49.224923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8de193c2477'
down_revision = '9b02a1331612'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('alter table todo alter column update on update now()')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
