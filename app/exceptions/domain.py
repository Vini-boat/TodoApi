class UserAlreadyExists(Exception):
    def __init__(self, detail: str = "User already exists"):
        self.detail = detail

class UserNotFound(Exception):
    def __init__(self, detail: str = "User not found"):
        self.detail = detail

class UserNotActive(Exception):
    def __init__(self, detail: str = "User is not active"):
        self.detail = detail

class TaskNotFound(Exception):
    def __init__(self, detail: str = "Task not found"):
        self.detail = detail

class CommentNotFound(Exception):
    def __init__(self, detail: str = "Comment not found"):
        self.detail = detail

class PermissionDenied(Exception):
    def __init__(self, detail: str = "Permission denied"):
        self.detail = detail