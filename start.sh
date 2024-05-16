#!/bin/bash

# Static fayllarni to'plash
python manage.py collectstatic --no-input

# Ma'lumotlar bazasi uchun o'zgartirishlar yaratish
python manage.py makemigrations --no-input

# Ma'lumotlar bazasini o'zgartirishlar bilan o'zgartirish
python manage.py migrate --no-input

# Django serverni ishga tushirish
gunicorn --bind 0.0.0.0:8001 dev.wsgi
