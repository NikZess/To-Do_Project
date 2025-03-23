from .database import get_connect_to_db

# 1. Добавление заметок
def add_note(note: str): # Аннотация типов
    """
    Функция добавление заметки
    """
    conn = get_connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (text) VALUES (?)", (note,))
    conn.commit()
    conn.close()

# 2. Удаление заметки
def delete_note(note_id: int):
    """
    Функция удаления заметки по ID
    """
    conn = get_connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

# 3. Обновление заметок
def update_note(note_id: int, new_text: str):
    """
    Функция обновления заметки по ID
    """
    conn = get_connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET text = ? WHERE id = ?", (new_text, note_id))
    conn.commit()
    conn.close()

# 4. Просмотр всех заметок
def get_notes():
    """
    Функция просмотра всех заметок
    """
    conn = get_connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = [{"id": row[0], "text": row[1]} for row in cursor.fetchall()]
    conn.close()
    return notes