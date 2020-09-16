"""Add student_sessions table

Revision ID: 6720bdea54fe
Revises: 3753b2e815c7
Create Date: 2020-09-16 21:07:11.160091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6720bdea54fe"
down_revision = "3753b2e815c7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "student_sessions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("student_id", sa.Integer(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("duration", sa.Integer(), nullable=False),
        sa.Column("session_type", sa.String(length=32), nullable=False),
        sa.Column("project", sa.String(length=32), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("progress", sa.String(length=32), nullable=False),
        sa.Column("concerns", sa.Text(), nullable=True),
        sa.Column("personal_notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["student_id"],
            ["students.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("student_sessions")
    # ### end Alembic commands ###
