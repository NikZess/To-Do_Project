const API_URL = "http://127.0.0.1:5050"; // Адрес API

// Функция получения заметок
async function getNotes() {
    const response = await fetch(`${API_URL}/notes`);
    const data = await response.json();
    const notesDiv = document.getElementById("notes");
    notesDiv.innerHTML = "";
    data.notes.forEach((note) => {
        const noteItem = document.createElement("div");
        noteItem.className = "note-item";
        noteItem.innerHTML = `
            <span>${note.text}</span>
            <div class="note-buttons">
                <button class="edit-btn" onclick="updateNote(${note.id}, '${note.text}')">✏️</button>
                <button class="delete-btn" onclick="deleteNote(${note.id})">❌</button>
            </div>
        `;
        notesDiv.appendChild(noteItem);
    });
}

// Функция добавления заметки
async function addNote() {
    const noteText = document.getElementById("noteInput").value;
    if (!noteText) return alert("Введите текст!");

    const response = await fetch(`${API_URL}/add?note=${encodeURIComponent(noteText)}`, {
        method: "POST"
    });

    if (response.ok) {
        document.getElementById("noteInput").value = "";
        await getNotes(); // Ждем обновления списка после добавления
    } else {
        alert("Ошибка при добавлении заметки");
    }
}

// Функция удаления заметки
async function deleteNote(id) {
    await fetch(`${API_URL}/delete/${id}`, { method: "DELETE" });
    getNotes();
}

// Функция обновления заметки
async function updateNote(id, oldText) {
    const newText = prompt("Введите новый текст:", oldText);
    if (!newText) return;

    await fetch(`${API_URL}/update/${id}?new_text=${encodeURIComponent(newText)}`, { method: "PUT" });
    getNotes();
}

// Загрузка заметок при старте
getNotes();