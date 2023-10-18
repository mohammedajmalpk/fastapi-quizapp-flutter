"""create_tables_user_mark_trackrecord

Revision ID: d6064758d2e9
Revises: 0e6a4e14ef68
Create Date: 2023-10-18 20:53:39.757344

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, String, DateTime, ARRAY, Float, func, ForeignKey


# revision identifiers, used by Alembic.
revision: str = 'd6064758d2e9'
down_revision: Union[str, None] = '0e6a4e14ef68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        Column('id',Integer, primary_key=True, index=True),
        Column('name', String, nullable=True),
        Column('phone', String, nullable=False),
        Column('created_at',DateTime(timezone=True), default=func.now())
    )

    op.create_table(
        'marks',
        Column('id',Integer, primary_key=True, index=True),
        Column('questionsAttended', ARRAY(Integer), default=[]),
        Column('answerSelected', ARRAY(Integer), default=[]),
        Column('correctAnswers', ARRAY(Integer), default=[]),
        Column('getMark', Integer, default=0, nullable=False),
        Column('percentage', Float, default=0.0, nullable=False),
        Column('created_at',DateTime(timezone=True), default=func.now())
    )

    op.create_table(
        'trackrecord',
        Column('id',Integer, primary_key=True, index=True),
        Column('user', Integer, ForeignKey('users.id')),
        Column('attempt', Integer, default=0, nullable=False),
        Column('mark', Integer, ForeignKey('marks.id')),
        Column('created_at',DateTime(timezone=True), default=func.now())
    )

def downgrade() -> None:
    pass
