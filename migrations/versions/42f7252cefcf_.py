"""empty message

Revision ID: 42f7252cefcf
Revises: 3ba403cc65f0
Create Date: 2025-02-21 18:09:10.964191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42f7252cefcf'
down_revision = '3ba403cc65f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('livros_create', schema=None) as batch_op:
        batch_op.add_column(sa.Column('materia', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('livros_create', schema=None) as batch_op:
        batch_op.drop_column('materia')

    # ### end Alembic commands ###
