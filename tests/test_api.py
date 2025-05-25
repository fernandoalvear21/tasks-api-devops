import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app  # Cambiamos 'from src.main import app' a 'from main import app'

client = TestClient(app)

# Prueba para la ruta principal
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Bienvenido a la API de Tareas de DevOps Maestro" in response.json()["message"]

# Pruebas para operaciones CRUD de tareas

# Variable para almacenar el ID de la tarea creada en las pruebas
task_id = None

def test_create_task():
    global task_id
    task_data = {
        "title": "Tarea de prueba",
        "description": "Esta es una tarea creada durante las pruebas",
        "completed": False
    }
    response = client.post("/api/v1/tasks/", json=task_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["description"] == task_data["description"]
    assert data["completed"] == task_data["completed"]
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data
    # Guardamos el ID para usarlo en otras pruebas
    task_id = data["id"]

def test_read_tasks():
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    # Verificar que la lista no esté vacía después de crear una tarea
    if task_id is not None:
        assert len(response.json()) > 0

def test_read_task():
    # Omitir si no se ha creado una tarea
    if task_id is None:
        pytest.skip("No hay tarea creada para probar")
    
    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert "title" in data
    assert "description" in data
    assert "completed" in data
    assert "created_at" in data
    assert "updated_at" in data

def test_update_task():
    # Omitir si no se ha creado una tarea
    if task_id is None:
        pytest.skip("No hay tarea creada para probar")
    
    update_data = {
        "title": "Tarea actualizada",
        "description": "Esta tarea ha sido actualizada durante las pruebas",
        "completed": True
    }
    response = client.put(f"/api/v1/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == update_data["title"]
    assert data["description"] == update_data["description"]
    assert data["completed"] == update_data["completed"]

def test_delete_task():
    # Omitir si no se ha creado una tarea
    if task_id is None:
        pytest.skip("No hay tarea creada para probar")
    
    response = client.delete(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 204
    
    # Verificar que la tarea ya no existe
    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 404

# Pruebas para casos de error

def test_read_nonexistent_task():
    # Usar un ID que probablemente no exista
    nonexistent_id = 9999
    response = client.get(f"/api/v1/tasks/{nonexistent_id}")
    assert response.status_code == 404

def test_update_nonexistent_task():
    # Usar un ID que probablemente no exista
    nonexistent_id = 9999
    update_data = {"title": "Esta tarea no existe"}
    response = client.put(f"/api/v1/tasks/{nonexistent_id}", json=update_data)
    assert response.status_code == 404

def test_delete_nonexistent_task():
    # Usar un ID que probablemente no exista
    nonexistent_id = 9999
    response = client.delete(f"/api/v1/tasks/{nonexistent_id}")
    assert response.status_code == 404

def test_create_invalid_task():
    # Datos inválidos (falta el título que es obligatorio)
    invalid_data = {
        "description": "Esta tarea no tiene título",
        "completed": False
    }
    response = client.post("/api/v1/tasks/", json=invalid_data)
    assert response.status_code == 422  # Unprocessable Entity