# Book Store API

Учебный проект в рамках обучения Octagon.

## Описание

REST API книжного магазина с использованием FastAPI
и базы данных PostgreSQL.

## Технологии

- Python 3
- Ubuntu (WSL 2)
- PostgreSQL
- SQLAlchemy
- FastAPI
- Uvicorn
- Pydantic
- psycopg2-binary
- python-dotenv

## Возможности

- CRUD для книг и категорий
- Фильтрация книг по категориям
- Валидация данных через Pydantic
- Подключение к PostgreSQL
- Автоматическая документация Swagger
- Проверка состояния сервера

## Запуск проекта

1. Запустить PostgreSQL.
2. Создать базу данных и пользователя.
3. Настроить файл .env.
4. Активировать виртуальное окружение.
5. Установить зависимости.

## Команды запуска

    source venv/bin/activate
    pip install -r requirements.txt
    python app/init_db.py
    uvicorn app.main:app --reload

## API

- Swagger: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health
- Books: http://127.0.0.1:8000/books/
- Categories: http://127.0.0.1:8000/categories/

## Скриншоты

Результаты тестирования API и PostgreSQL
находятся в папке examples/.