"""empty message

Revision ID: 9ca96198ab2e
Revises: d20bcab1d029
Create Date: 2020-02-18 18:11:59.005429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ca96198ab2e'
down_revision = 'd20bcab1d029'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Template_para1_key', 'Template', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('Template_para1_key', 'Template', ['para1'])
    # ### end Alembic commands ###
