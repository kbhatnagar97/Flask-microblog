"""empty message

Revision ID: 59c60dcafcec
Revises: b9b702afb147
Create Date: 2020-02-20 11:44:18.586198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59c60dcafcec'
down_revision = 'b9b702afb147'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Customer_email', table_name='Customer')
    op.create_index(op.f('ix_Customer_email'), 'Customer', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Customer_email'), table_name='Customer')
    op.create_index('ix_Customer_email', 'Customer', ['email'], unique=False)
    # ### end Alembic commands ###
