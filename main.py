from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешить запросы с любых доменов
    allow_credentials=True,
    allow_methods=["*"], # Разрешить все методы (GET, POST, PUT, DELETE)
    allow_headers=["*"], # Разрешить все заголовки
)

def init_db():
    """
    Функция инициализация БД
    """
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# 1. Добавление заметок
@app.post("/add", summary="Добавление заметки")
def add_note(note: str): # Аннотация типов
    """
    Функция добавление заметки
    """
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (text) VALUES (?)", (note,))
    conn.commit()
    conn.close()
    return {"message": "Заметка добавлена"}

# 2. Удаление заметки
@app.delete("/delete/{note_id}", summary="Удаление заметки")
def delete_note(note_id: int):
    """
    Функция удаления заметки по ID
    """
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    return {"message": "Заметка удалена"}

# 3. Обновление заметок
@app.put("/update/{note_id}", summary="Обновление заметки")
def update_note(note_id: int, new_text: str):
    """
    Функция обновления заметки по ID
    """
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET text = ? WHERE id = ?", (new_text, note_id))
    conn.commit()
    conn.close()
    return {"message": "Заметка обновлена"}

# 4. Просмотр всех заметок
@app.get("/notes", summary="Показ всех заметок")
def get_notes():
    """
    Функция просмотра всех заметок
    """
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = [{"id": row[0], "text": row[1]} for row in cursor.fetchall()]
    conn.close()
    return {"notes": notes}

# Запуск сервера
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5050)