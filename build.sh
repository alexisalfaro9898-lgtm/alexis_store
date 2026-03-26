#!/usr/bin/env bash
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Generar archivos estáticos
python manage.py collectstatic --no-input

# --- ESTO ES LO QUE ARREGLA LA TABLA ---
python manage.py makemigrations --no-input
python manage.py migrate --no-input
