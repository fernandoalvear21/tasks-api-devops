#!/bin/bash

# Asegurar que el directorio de datos existe y tiene los permisos correctos
mkdir -p /data
chmod 777 /data

# Inicializar la base de datos
python src/init_db.py

# Verificar si la inicialización fue exitosa
if [ $? -eq 0 ]; then
    echo "Base de datos inicializada correctamente"
    # Iniciar la aplicación
    python main.py
else
    echo "Error al inicializar la base de datos"
    exit 1
fi