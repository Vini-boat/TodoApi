from fastapi import HTTPException

class UserNotFoundHTTP(HTTPException):
    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=404, detail=detail) 

class InvalidCredentialsHTTP(HTTPException):
    def __init__(self, detail: str = "Invalid email or password"):
        super().__init__(status_code=401, detail=detail, headers={"WWW-Authenticate": "Bearer"})

class UserAlreadyExistsHTTP(HTTPException):
    def __init__(self, detail: str = "User already exists"):
        super().__init__(status_code=409, detail=detail)

class UserNotActiveHTTP(HTTPException):
    def __init__(self, detail: str = "User is not active"):
        super().__init__(status_code=403, detail=detail)

class TaskNotFoundHTTP(HTTPException):
    def __init__(self, detail: str = "Task not found"):
        super().__init__(status_code=404, detail=detail)

class CommentNotFoundHTTP(HTTPException):
    def __init__(self, detail: str = "Comment not found"):
        super().__init__(status_code=404, detail=detail)

class PermissionDeniedHTTP(HTTPException):
    def __init__(self, detail: str = "Permission denied"):
        super().__init__(status_code=403, detail=detail)