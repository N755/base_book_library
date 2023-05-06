from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = "ffb29eb78058"
down_revision = "f3b5709a8967"
branch_labels = None
depends_on = None


def upgrade():
    # add the borrowed column to the book table
    op.add_column(
        "book", sa.Column("borrowed", sa.Boolean(), nullable=False, server_default="0")
    )


def downgrade():
    # remove the borrowed column from the book table
    op.drop_column("book", "borrowed")
