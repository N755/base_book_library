"""empty message

Revision ID: f3b5709a8967
Revises: 89cb5f189487
Create Date: 2023-05-07 00:15:45.278407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f3b5709a8967"
down_revision = "89cb5f189487"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("_alembic_tmp_book")
    with op.batch_alter_table("book", schema=None) as batch_op:
        batch_op.add_column(
            "book",
            sa.Column("borrowed", sa.Boolean(), nullable=False, server_default="0"),
        )

        batch_op.drop_column("id")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("book", schema=None) as batch_op:
        batch_op.op.add_column(
            "book",
            sa.Column("borrowed", sa.Boolean(), nullable=False, server_default="0"),
        )

        batch_op.drop_column("borrowed")

    op.create_table(
        "_alembic_tmp_book",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("title", sa.VARCHAR(length=50), nullable=False),
        sa.Column("author", sa.VARCHAR(length=50), nullable=False),
        sa.Column("publisher", sa.VARCHAR(length=50), nullable=False),
        sa.Column("year", sa.INTEGER(), nullable=False),
        sa.Column("pages", sa.INTEGER(), nullable=False),
        sa.Column("borrowed", sa.BOOLEAN(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###
