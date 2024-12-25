import { useState, useEffect } from "react";
import api from "../api";
import Note from "../components/Note"
import "../styles/Home.css"

function Home() {
    const [notes, setNotes] = useState([]);
    const [content, setContent] = useState("");
    const [title, setTitle] = useState("");

    useEffect(() => {
        getNotes();
    }, []);

    const getNotes = () => {
        api
            .get("/api/note/")
            .then((res) => res.data)
            .then((data) => {
                setNotes(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    const deleteNote = (id) => {
        api
            .delete(`/api/note/delete/${id}/`)
            .then((res) => {
                if (res.status === 204) alert("Задача удалена!");
                else alert("Ошибка удаления");
                getNotes();
            })
            .catch((error) => alert(error));
    };

    const createNote = (e) => {
        e.preventDefault();
        api
            .post("/api/note/", { content, title })
            .then((res) => {
                if (res.status === 201) alert("Задача создана!)");
                else alert("Ошибка при создании задачи(((");
                getNotes();
            })
            .catch((err) => alert(err));
    };

    return (
        <div>
            <div>
                <h2>Задачи</h2>
                {notes.map((note) => (
                    <Note note={note} onDelete={deleteNote} key={note.id} />
                ))}
            </div>
            <h2>Создать задачу</h2>
            <form onSubmit={createNote}>
                <label htmlFor="title">Название:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value={title}
                />
                <label htmlFor="content">Описание:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                ></textarea>
                <br />
                <input type="submit" value="Отправить"></input>
            </form>
        </div>
    );
}

export default Home;