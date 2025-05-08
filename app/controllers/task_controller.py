from fastapi import APIRouter, Depends, HTTPException
from app.services.task_service import TaskService
from app.schemas.task import TaskResponse#, TaskCreate, TaskUpdate

router = APIRouter()

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task_by_id(
    task_id: int,
    service: TaskService = Depends(TaskService)
    ):
    task = service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task