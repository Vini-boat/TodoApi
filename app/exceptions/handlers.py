from fastapi import FastAPI

from app.exceptions.domain import UserNotFound as UserNotFoundDomain
from app.exceptions.http import UserNotFound as UserNotFoundHTTP

from app.exceptions.domain import UserAlreadyExists as UserAlreadyExistsDomain
from app.exceptions.http import UserAlreadyExists as UserAlreadyExistsHTTP

from app.exceptions.domain import UserNotActive as UserNotActiveDomain
from app.exceptions.http import UserNotActive as UserNotActiveHTTP

from app.exceptions.domain import TaskNotFound as TaskNotFoundDomain
from app.exceptions.http import TaskNotFound as TaskNotFoundHTTP

def register_exception_handlers(app: FastAPI):

    @app.exception_handler(UserNotFoundDomain)
    async def user_not_found_handler(request, exc: UserNotFoundDomain):
        raise UserNotFoundHTTP(detail=exc.detail)

    @app.exception_handler(UserAlreadyExistsDomain)
    async def user_already_exists_handler(request, exc: UserAlreadyExistsDomain):
        raise UserAlreadyExistsHTTP(detail=exc.detail)
    
    @app.exception_handler(UserNotActiveDomain)
    async def user_not_active_handler(request, exc: UserNotActiveDomain):
        raise UserNotActiveHTTP(detail=exc.detail)
    
    @app.exception_handler(TaskNotFoundDomain)
    async def task_not_found_handler(request, exc: TaskNotFoundDomain):
        raise TaskNotFoundHTTP(detail=exc.detail)