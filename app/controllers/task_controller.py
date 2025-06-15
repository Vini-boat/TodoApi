from fastapi import APIRouter, Depends, Query
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
    return service.get_task_by_id(task_id)

@router.get("/tasks", response_model=Optional[List[TaskResponse]])
async def get_tasks_assigned_to_user(
    user_id: int = Query(..., alias="assignedTo"),
    service: TaskService = Depends(TaskService)
    ):
    return service.get_tasks_assigned_to_user(user_id)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int, 
    task: TaskUpdate, 
    service: TaskService = Depends(TaskService)
    ):
    return service.update_task(task_id, task)

@router.delete("/tasks/{task_id}", response_model=TaskResponse)
async def delete_task(
    task_id: int, 
    service: TaskService = Depends(TaskService)
    ):
    return service.delete_task(task_id)