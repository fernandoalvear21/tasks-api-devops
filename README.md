# DevOps Maestro - API de Tareas

Este proyecto es una API REST para gestionar tareas, desarrollada como parte del proyecto "DevOps Maestro" para practicar habilidades de DevOps.

## Tecnologías utilizadas

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (desarrollo)
- Docker
- CI/CD (próximamente)
- Terraform (próximamente)
- Monitoreo (próximamente)

## Configuración del entorno de desarrollo

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd DevOps-project001
````
2. Crear y activar el entorno virtual:
```bash
python -m venv venv
source venv/bin/activate
```
3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```
4. Inicializar la base de datos:
```bash
python src/init_db.py
```
5. Ejecutar la aplicación:
```bash 
cd src
python main.py
```