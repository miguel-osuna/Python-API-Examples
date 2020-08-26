"""empty message

Revision ID: 5957c18b723a
Revises: f3583338f4a9
Create Date: 2020-08-25 21:44:54.403205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5957c18b723a'
down_revision = 'f3583338f4a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notification', sa.Column('notification_category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'notification', 'notification_category', ['notification_category_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notification', type_='foreignkey')
    op.drop_column('notification', 'notification_category_id')
    # ### end Alembic commands ###
