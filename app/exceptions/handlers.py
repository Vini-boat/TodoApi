from fastapi import FastAPI

from app.exceptions.domain import PermissionDenied as PermissionDeniedDomain
from app.exceptions.http import PermissionDeniedHTTP

from app.exceptions.domain import UserNotFound as UserNotFoundDomain
from app.exceptions.http import UserNotFoundHTTP

from app.exceptions.domain import UserAlreadyExists as UserAlreadyExistsDomain
from app.exceptions.http import UserAlreadyExistsHTTP

from app.exceptions.domain import UserNotActive as UserNotActiveDomain
from app.exceptions.http import UserNotActiveHTTP

from app.exceptions.domain import TaskNotFound as TaskNotFoundDomain
from app.exceptions.http import TaskNotFoundHTTP

from app.exceptions.domain import CommentNotFound as CommentNotFoundDomain
from app.exceptions.http import CommentNotFoundHTTP

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
    
    @app.exception_handler(CommentNotFoundDomain)
    async def comment_not_found_handler(request, exc: CommentNotFoundDomain):
        raise CommentNotFoundHTTP(detail=exc.detail)
    
    @app.exception_handler(PermissionDeniedDomain)
    async def permission_denied_handler(request, exc: PermissionDeniedDomain):
        raise PermissionDeniedHTTP(detail=exc.detail)