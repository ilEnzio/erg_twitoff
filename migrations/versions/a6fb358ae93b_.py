"""empty message

Revision ID: a6fb358ae93b
Revises: b69b8679e110
Create Date: 2020-09-16 11:01:18.567775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6fb358ae93b'
down_revision = 'b69b8679e110'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweet', sa.Column('num_embedding', sa.PickleType(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tweet', 'num_embedding')
    # ### end Alembic commands ###
