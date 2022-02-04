"""init

Revision ID: e0384324e1ac
Revises: 
Create Date: 2022-01-27 17:54:38.908632

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e0384324e1ac'
down_revision = None
branch_labels = None
depends_on = None


# in case of changes: alembic downgrade base && alembic upgrade head
def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('full_name', sa.String, nullable=False),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False)
    )

    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('author', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('books')
