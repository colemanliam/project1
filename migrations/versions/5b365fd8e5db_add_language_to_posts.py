"""add language to posts

Revision ID: 5b365fd8e5db
Revises: 81f33c9c25d5
Create Date: 2022-06-06 20:18:51.895562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b365fd8e5db'
down_revision = '81f33c9c25d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
