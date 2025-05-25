from fastapi import FastAPI
from api.routes import tasks  # Cambiado de 'from src.api.routes import tasks'

app = FastAPI(
    title="DevOps Maestro - API de Tareas",
    description="API REST para gestionar tareas como parte del proyecto DevOps Maestro",
    version="0.1.0"
)

app.include_router(tasks.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Tareas de DevOps Maestro"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)