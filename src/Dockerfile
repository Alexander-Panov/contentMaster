FROM python:3

# Задать переменные среды
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Задать рабочий каталог
WORKDIR /content_master

# Установить зависимости
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Django project
COPY . .