"""Renaming students to scholars

Revision ID: a0a405ae501c
Revises: 
Create Date: 2025-05-27 16:45:54.204912

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0a405ae501c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    """Downgrade schema."""
    op.rename_table('scholars', 'students')
