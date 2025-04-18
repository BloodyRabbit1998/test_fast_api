
# О проекте

REST API-сервис для бронирования столиков в ресторане. Реализован на FastAPI, с использованием PostgreSQL и Docker.

---

## 🚀 Возможности

- 📋 Управление столиками (создание, удаление, просмотр)
- 📅 Бронирование столиков на определённое время
- 🛡️ Защита от конфликтов бронирования
- 🧱 Миграции через Alembic
- 🧪 Тесты на pytest

## 📦 Стек технологий

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Docker & Docker Compose](https://docs.docker.com/compose/)
- [Pytest](https://docs.pytest.org/)

---
## 🛠️ Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/BloodyRabbit1998/test_fast_api.git
cd test_fast_api
```
### 2. Настроить переменные окружения

Создайте файл .env на основе .env.example:
```bash
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=database_name
HOST_DB_PORT=5432
POSTGRES_HOST=db
```
У вас уже должен быть установлен [PostgreSQL](https://www.postgresql.org/download/) и создана [база данных](https://www.postgresql.org/docs/current/sql-createdatabase.html).
Вместо `username` и `password` ввести свои данные указаные при создании базы данных
Вместо `database_name` вводите название своей базы данных
Если собираетесь запустить проект в Docker, то оставте `POSTGRES_HOST`  со значением `db`, для локального запуска или подключения удаленой БД ввести адресс (локально `127.0.0.1`)
#### не забудьте сохранить файл

### 3. Запуск через Docker Compose
У вас уже должен быть установлен [Docker](https://www.docker.com/products/docker-desktop/)
```bash
docker-compose up --build
```
Приложение будет доступно по адресу:

📍 http://localhost:8000


если будет ошибка:
`Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:5432 -> 127.0.0.1:0: listen tcp 0.0.0.0:5432: bind: address already in use`
нужно изменить в файле `.env` перемную `HOST_DB_PORT` на другое значение 
### Проверка работы и документация: http://localhost:8000/docs

### 4. Выполните миграцию:
 Зайди внутрь контейнера web:
 ```bash
 docker exec -it fastapi_app bash
 ```
Затем введите слудещие команды:
 ```bash
alembic revision --autogenerate -m "create tables"    
alembic upgrade head                         
```
## Запуск тестов

Для запуска тестов введите следующию команду

```bash
  npm run test
```


## Запуск локально

### 1. Клонировать репозиторий

```bash
git clone https://github.com/BloodyRabbit1998/test_fast_api.git
cd test_fast_api
```
### 2. Настроить переменные окружения

Создайте файл .env на основе .env.example:
```bash
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=database_name
```
У вас уже должен быть установлен [PostgreSQL](https://www.postgresql.org/download/) и создана [база данных](https://www.postgresql.org/docs/current/sql-createdatabase.html).
Вместо `username` и `password` ввести свои данные указаные при создании базы данных
Вместо `database_name` вводите название своей базы данных
#### не забудьте сохранить файл

### 3. Установить пакеты
на Windows
```bash
  pip install -r requirements.txt
```
на Unix системах

```bash
  pip3 install -r requirements.txt
```
### 4. Выполните миграцию:
 Зайди внутрь контейнера web:
 ```bash
 docker exec -it fastapi_app bash
 ```
Затем введите слудещие команды:
 ```bash
alembic revision --autogenerate -m "create tables"    
alembic upgrade head                         
```
### 5. Запуск приложения
```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```



