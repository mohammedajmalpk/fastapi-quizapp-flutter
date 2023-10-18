from fastapi import FastAPI
import uvicorn

from app.database import engine
from app.api.router import quiz_router
from app.models import quizmodel

app = FastAPI()

app.include_router(quiz_router.router)

quizmodel.Base.metadata.create_all(bind = engine)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)