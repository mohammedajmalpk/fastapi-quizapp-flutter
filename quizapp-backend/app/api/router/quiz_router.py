from multiprocessing import context
import re
from fastapi import APIRouter, Depends, HTTPException
from app.api.schema.quiz_schema import answerCreateRequest, answerUpdateRequest, questionCreateRquest, questionUpdateRequest
from sqlalchemy.orm import Session
from app.dependancies import get_db
from app.models.quizmodel import Answers, Questions
from starlette import status


router = APIRouter(
    prefix="/quiz",
    tags=["Quiz App"]
)

@router.post("/question/create")
async def question_create(request:questionCreateRquest, db: Session = Depends(get_db)):
    """
        api for create new question
    """
    try:
        new_question = Questions(
            question = request.question
        )
        db.add(new_question)
        db.commit()
        return {"detail":"New Question Created", "status": status.HTTP_201_CREATED}
    finally:
        db.close()


@router.post("/question/update")
async def question_update(request: questionUpdateRequest, db:Session = Depends(get_db)):
    """
        api for update question
    """
    try:
        is_existed_question = db.query(Questions).filter(
            Questions.id == request.id
        ).first()
        if is_existed_question is None:
            raise HTTPException(detail="Question Not Found", status_code=status.HTTP_404_NOT_FOUND)
        is_existed_question.question = request.question
        db.commit()
        return {"detail":"Question Updated", "status":status.HTTP_200_OK}
    finally:
        db.close()


@router.post("/answer/create")
async def create_answer(request: answerCreateRequest, db: Session = Depends(get_db)):
    try:
        new_answer = Answers(
            questionId = request.questionId,
            answer = request.answer,
            is_correct = request.is_correct
        )
        db.add(new_answer)
        db.commit()
        return {"detail": "New Answer Created", "status": status.HTTP_201_CREATED}
    finally:
        db.close()


@router.put("/answer/update")
async def create_answer(request: answerUpdateRequest, db: Session = Depends(get_db)):
    try:
        is_existed_answer = db.query(Answers).filter(
            Answers.id == request.id
        ).first()

        if is_existed_answer is None:
            raise HTTPException(detail="Answer Not Found", status_code=status.HTTP_404_NOT_FOUND)
        is_existed_answer.is_correct = request.is_correct
        is_existed_answer.answer = request.answer
        is_existed_answer.questionId = request.questionId
        db.commit()
        return {"detail": "Answer Updated", "status": status.HTTP_201_CREATED}
    finally:
        db.close()

@router.get("/question-answer/all/{questionid}")
async def fetch_all_questions_answers(questionid: int,db:Session=Depends(get_db)):
    try:
        is_existed_question_answers = db.query(Questions).filter(
            Questions.id == questionid
        ).first()
        if is_existed_question_answers is None:
            raise HTTPException(detail="No Questions Found", status_code=status.HTTP_404_NOT_FOUND)
        context = {
            "question":is_existed_question_answers.question,
            "answers":[{"id":i.id, "answer": i.answer} for i in is_existed_question_answers.answer]
        }
        return {"detail":context, "status":status.HTTP_200_OK}
    finally:
        db.close()

@router.get("/question-correct-answer/all")
async def fetch_all_questions_correct_answers(db:Session=Depends(get_db)):
    try:
        is_existed_question_answers = db.query(Questions).order_by('id').all()
        if is_existed_question_answers is None:
            raise HTTPException(detail="No Questions Found", status_code=status.HTTP_404_NOT_FOUND)
        context = [
            {
                "question_answer": [
                    {
                        "questionId": item.id,
                        "question": item.question,
                        "answer": i.answer,
                        "answerId":i.id
                    } for i in item.answer if i.is_correct == True]
            } for item in is_existed_question_answers
        ]
        return {"detail":context, "status":status.HTTP_200_OK}
    finally:
        db.close()