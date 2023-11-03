from numbers import Integral
from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, ARRAY, Float
from sqlalchemy.orm import relationship
from datetime import datetime


class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())

    answer = relationship('Answers', back_populates='question')

    def __str__(self):
        return self.id

class Answers(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    questionId = Column(Integer, ForeignKey(Questions.id))
    answer = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())

    question = relationship("Questions", back_populates='answer')

    def __str__(self):
        return self.id


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())


class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)
    questionsAttended = Column(ARRAY(Integer), default=[]) # all attendad question Ids
    answerSelected = Column(ARRAY(Integer), default=[]) # all attendad answer Ids
    correctAnswers = Column(ARRAY(Integer), default=[]) # correct answer Ids
    getMark = Column(Integer, default=0, nullable=False) # correct answer Ids * 10
    percentage = Column(Float, default=0.0, nullable=False) # (getmark / total mark) *100
    created_at = Column(DateTime(timezone=True), default=datetime.now())


class TrackRecord(Base):
    """
        after submission Trackrecord automatically created.
    """
    __tablename__ = "trackrecord"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey(User.id))
    attempt = Column(Integer, default=0, nullable=False)
    mark = Column(Integer, ForeignKey(Mark.id))
    created_at = Column(DateTime(timezone=True), default=datetime.now())

    userdetails = relationship('User')
    markdetails = relationship('Mark', join_depth=2)