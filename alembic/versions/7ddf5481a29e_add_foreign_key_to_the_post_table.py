"""Add foreign key to the post table

Revision ID: 7ddf5481a29e
Revises: f1dfb5436b2e
Create Date: 2022-09-06 14:00:40.608280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ddf5481a29e'
down_revision = 'f1dfb5436b2e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", 
        sa.Column("user_id", sa.Integer, nullable=False))
    op.create_foreign_key("user_id_fkey", source_table="posts", referent_table="users",
     local_cols=["user_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("user_id_fkey", table_name="posts")
    op.drop_column("posts", "user_id")
    pass
