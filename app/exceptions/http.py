from fastapi import HTTPException

class UserNotFound(HTTPException):
    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=404, detail=detail) 

class InvalidCredentials(HTTPException):
    def __init__(self, detail: str = "Invalid email or password"):
        super().__init__(status_code=401, detail=detail, headers={"WWW-Authenticate": "Bearer"})

class UserAlreadyExists(HTTPException):
    def __init__(self, detail: str = "User already exists"):
        super().__init__(status_code=409, detail=detail)

class UserNotActive(HTTPException):
    def __init__(self, detail: str = "User is not active"):
        super().__init__(status_code=403, detail=detail)

class TaskNotFound(HTTPException):
    def __init__(self, detail: str = "Task not found"):
        super().__init__(status_code=404, detail=detail)

class CommentNotFound(HTTPException):
    def __init__(self, detail: str = "Comment not found"):
        super().__init__(status_code=404, detail=detail)

class PermissionDenied(HTTPException):
    def __init__(self, detail: str = "Permission denied"):
        super().__init__(status_code=403, detail=detail)