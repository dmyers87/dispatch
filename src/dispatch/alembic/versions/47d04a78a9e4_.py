"""Removes deprecated columns in participant model

Revision ID: 47d04a78a9e4
Revises: b3bf2da9be17
Create Date: 2021-05-13 17:32:24.795570

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "47d04a78a9e4"
down_revision = "b3bf2da9be17"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("participant", "is_active")
    op.drop_column("participant", "inactive_at")
    op.drop_column("participant", "active_at")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "participant",
        sa.Column("active_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "participant",
        sa.Column("inactive_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "participant", sa.Column("is_active", sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
