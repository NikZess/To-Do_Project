from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from app.api import endpoints

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешить запросы с любых доменов
    allow_credentials=True,
    allow_methods=["*"], # Разрешить все методы (GET, POST, PUT, DELETE)
    allow_headers=["*"], # Разрешить все заголовки
)

# Инициализация бд
init_db()

# Подключение маршрутов
app.include_router(endpoints.router)
