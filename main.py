from fastapi import FastAPI

from domain.question import question_router
from domain.user import user_router

app = FastAPI()

app.include_router(question_router.router)
app.include_router(user_router.router)