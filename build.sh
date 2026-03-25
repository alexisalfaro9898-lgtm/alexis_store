#!/usr/bin/env bash
# Salir si hay un error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos (CSS, Imágenes)
python manage.py collectstatic --no-input

# Aplicar migraciones de la base de datos
python manage.py migrate
