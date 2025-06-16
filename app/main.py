from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.controllers.user_controller import router as user_router
from app.controllers.task_controller import router as task_router
from app.controllers.auth_controller import router as auth_router
from app.controllers.comment_controller import router as comment_router

from app.infraestructure.sqlite import create_all_tables
from app.exceptions.handlers import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_all_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/api/v1", tags=["auth"])
app.include_router(user_router, prefix="/api/v1", tags=["users"])
app.include_router(task_router, prefix="/api/v1", tags=["tasks"])
app.include_router(comment_router, prefix="/api/v1", tags=["comments"])

register_exception_handlers(app)
