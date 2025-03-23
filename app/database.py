import sqlite3

def get_connect_to_db():
    return sqlite3.connect("notes.db")

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