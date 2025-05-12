from fastapi import HTTPException

UserNotFound = HTTPException(status_code=404, detail="User not found")