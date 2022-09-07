"""Create a post table

Revision ID: 24c881db7a3d
Revises: 
Create Date: 2022-09-06 12:49:28.428649

"""
import ssl
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24c881db7a3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
     sa.Column("id", sa.Integer(), nullable = False),
     sa.Column("title", sa.String(), nullable= False),
     sa.Column("content", sa.String(), nullable=False),
     sa.Column("published", sa.Boolean(), nullable = False, server_default = "TRUE"),
     sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default = sa.text("now()")),
     sa.PrimaryKeyConstraint("id"),
     )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
