"""Create a user Table

Revision ID: a8942e856232
Revises: 24c881db7a3d
Create Date: 2022-09-06 13:12:13.128993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8942e856232'
down_revision = '24c881db7a3d'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table("users", 
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default= sa.text("now()")),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:

    op.drop_table("users")
    pass
