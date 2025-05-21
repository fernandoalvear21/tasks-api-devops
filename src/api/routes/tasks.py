from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from api.database import get_db
from api.models.schemas import TaskCreate, TaskUpdate, TaskInDB
from api.services import task_service

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "No encontrado"}},
)

@router.post("/", response_model=TaskInDB, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db=db, task=task)

@router.get("/", response_model=List[TaskInDB])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = task_service.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.get("/{task_id}", response_model=TaskInDB)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_service.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task

@router.put("/{task_id}", response_model=TaskInDB)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = task_service.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task_service.update_task(db=db, task_id=task_id, task=task)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_service.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    task_service.delete_task(db=db, task_id=task_id)
    return None