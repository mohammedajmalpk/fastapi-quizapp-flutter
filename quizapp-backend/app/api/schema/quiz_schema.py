from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class questionBaseRequest(BaseModel):
    id: Optional[int] = None
    question: Optional[str] = None
    created_at: Optional[datetime] = None


class answerBaseRequest(BaseModel):
    id: Optional[int] = None
    questionId: Optional[int] = None
    answer: Optional[str] = None
    is_correct: Optional[bool] = None
    created_at: Optional[datetime] = None


class questionCreateRquest(questionBaseRequest):
    question: str


class answerCreateRequest(answerBaseRequest):
    questionId: int
    answer: str
    is_correct: bool


class questionUpdateRequest(questionBaseRequest):
    id: int
    question: str


class answerUpdateRequest(answerBaseRequest):
    id: int
    questionId: int
    answer: str
    is_correct: bool


class UserBaseRequest(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    createdAt: Optional[datetime] = None


class UserCreateRequest(UserBaseRequest):
    name: str


class UserUpdateRequest(UserBaseRequest):
    id: int
    name: Optional[str]
    phone: Optional[str]


class questionWithAnswer(BaseModel):
    attendedAnswerIds: Optional[list] = [] # answer id
    attendedQuestionIds: Optional[list] = [] # question id
    correctAnswersIds : Optional[list] = []