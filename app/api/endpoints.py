from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from ..utils.templates import templates
from app import crud

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/add", summary="Добавление заметки")
def add_note(note: str):
    """
    Функция добавления заметки
    """
    crud.add_note(note)
    return {"message": "Заметка добавлена"}

@router.delete("/delete/{note_id}", summary="Удаление заметки")
def delete_note(note_id: int):
    """
    Функция удаления заметки по id
    """
    crud.delete_note(note_id)
    return {"message": "Заметка удалена"}

@router.put("/update/{note_id}", summary="Обновление заметки")
def update_note(note_id: int, new_text: str):
    """
    Функция обновления заметки по id
    """
    crud.update_note(note_id, new_text)
    return {"message": "Заметка обновлена"}

@router.get("/notes", summary="Показ заметок")
def get_notes():
    """
    Функция показа всех заметок
    """
    return {"notes": crud.get_notes()}