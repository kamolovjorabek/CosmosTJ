# Python 3.11 asosiy obrazini tanlash
FROM python:3.11

# Python uchun muhim o'zgaruvchilarni sozlash
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8001
# Pipni yangilash
RUN pip install --upgrade pip

# Tizim paketlarini o'rnatish
RUN apt update && apt -y install gcc libjpeg-dev libxslt-dev libpq-dev \
    libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

# Foydalanuvchi yaratish
RUN useradd -rms /bin/bash app

# Ishlash uchun katalogni belgilash
WORKDIR /app

# Static va staticfiles kataloglarini yaratish va huquqlarni sozlash
RUN mkdir /app/static /app/staticfiles \
    && chown -R app:app /app \
    && chmod 755 /app

# Barcha fayllarni /app katalogiga nusxalash va foydalanuvchi huquqlarini sozlash
COPY --chown=app:app . .

# Kerakli Python paketlarini o'rnatish
COPY requirements.txt /app/
RUN pip install -r requirements.txt
