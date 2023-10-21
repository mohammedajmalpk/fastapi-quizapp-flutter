import re
from fastapi import APIRouter, Depends, HTTPException
from app.api.schema.quiz_schema import questionCreateRquest, questionUpdateRequest
from sqlalchemy.orm import Session
from app.dependancies import get_db
from app.models.quizmodel import Questions
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
