"""unique-constraint-to-user-predictions

Revision ID: 582a93a2087b
Revises: 9886b715c6ae
Create Date: 2025-04-03 19:24:54.267117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '582a93a2087b'
down_revision: Union[str, None] = '9886b715c6ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('_user_league_uc', 'predictions', ['user_id', 'league_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('_user_league_uc', 'predictions', type_='unique')
    # ### end Alembic commands ###
