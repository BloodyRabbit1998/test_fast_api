"""Create tables

Revision ID: 9aaf85eb666a
Revises: d8a96ce396ce
Create Date: 2025-04-18 06:40:49.469376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9aaf85eb666a'
down_revision: Union[str, None] = 'd8a96ce396ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Столики',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('seats', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_Столики_id'), 'Столики', ['id'], unique=False)
    op.create_table('Бронирование',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_name', sa.String(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=False),
    sa.Column('reservation_time', sa.DateTime(), nullable=False),
    sa.Column('duration_minutes', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['table_id'], ['Столики.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Бронирование_id'), 'Бронирование', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Бронирование_id'), table_name='Бронирование')
    op.drop_table('Бронирование')
    op.drop_index(op.f('ix_Столики_id'), table_name='Столики')
    op.drop_table('Столики')
    # ### end Alembic commands ###
