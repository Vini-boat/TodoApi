from fastapi import APIRouter, Depends, HTTPException, Query
from app.services.task_service import TaskService
from app.dtos.task import TaskResponse, TaskCreate, TaskUpdate
from typing import Optional, List

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
async def create_new_task(
    task: TaskCreate, 
    service: TaskService = Depends(TaskService)
    ):
    created_task = service.create_task(task)
    return created_task

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task_by_id(
    task_id: int,
    service: TaskService = Depends(TaskService)
    ):
    task = service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/tasks", response_model=Optional[List[TaskResponse]])
async def get_tasks_assigned_to_user(
    user_id: int = Query(..., alias="assignedTo"),
    service: TaskService = Depends(TaskService)
    ):
    tasks = service.get_tasks_assigned_to_user(user_id)
    return tasks

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int, 
    task: TaskUpdate, 
    service: TaskService = Depends(TaskService)
    ):
    updated_task = service.update_task(task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/tasks/{task_id}", response_model=TaskResponse)
async def delete_task(
    task_id: int, 
    service: TaskService = Depends(TaskService)
    ):
    deleted_task = service.delete_task(task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task