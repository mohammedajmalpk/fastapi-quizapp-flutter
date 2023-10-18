"""create_tables_questions_answers

Revision ID: 0e6a4e14ef68
Revises:
Create Date: 2023-09-28 20:01:38.082349

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,Boolean
from app.models.quizmodel import Questions

# revision identifiers, used by Alembic.
revision: str = '0e6a4e14ef68'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "questions",
        Column('id', Integer, primary_key=True, index=True),
        Column('question', String, nullable=False),
        Column('created_at', DateTime(timezone=True), default=datetime.now())
    )

    op.create_table(
        "answers",
        Column('id', Integer, primary_key=True, index=True),
        Column('questionId', Integer, ForeignKey(Questions.id)),
        Column('answer', String, nullable=False),
        Column('is_correct', Boolean, default=False, nullable=False),
        Column('created_at', DateTime(timezone=True), default=datetime.now())
    )


def downgrade() -> None:
    pass
