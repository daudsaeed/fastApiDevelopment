"""empty message

Revision ID: f1dfb5436b2e
Revises: a8942e856232
Create Date: 2022-09-06 13:27:58.401801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1dfb5436b2e'
down_revision = 'a8942e856232'
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

