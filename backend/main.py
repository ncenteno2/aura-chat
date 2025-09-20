from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3


def init_db():
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    );
    """
    )
    con.commit()
    con.close()


def init_message_db():
    con = sqlite3.connect("messages.db")
    cursor = con.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS messages (
        message TEXT NOT NULL
    );
    """
    )
    con.commit()
    con.close()

class User(BaseModel):
    username: str
    password: str

class ChatMessage(BaseModel):
    message: str


init_db()

init_message_db()


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Aura Chat"}


@app.get("/users")
async def get_users():
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    con.close()
    return {"users": rows}


@app.post("/register")
async def register(user: User):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (user.username,))
    result = cursor.fetchone()

    if result:
        con.close()
        return {"message": "El usuario ya existe"}

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (user.username, user.password),
    )
    con.commit()
    con.close()
    return {"message": "Usuario registrado exitosamente"}


@app.post("/login")
async def login(user: User):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (user.username, user.password),
    )
    result = cursor.fetchone()
    con.close()

    if result:
        return {"message": "Inicio de sesión exitoso"}
    return {"message": "Nombre de usuario o contraseña incorrectos"}


@app.get("/chat")
async def get_chat():
    con = sqlite3.connect("messages.db")
    cursor = con.cursor()
    cursor.execute("SELECT message FROM ChatMessage")
    rows = cursor.fetchall()
    con.close()
    messages = [row[0] for row in rows]
    return {"messages": messages}


@app.post("/chat")
async def send_message(message: ChatMessage):
    con = sqlite3.connect("messages.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM messages")
    result = cursor.fetchone()
    cursor.execute(
        "INSERT INTO messages (message) VALUES (?)",
        (message.message,),
    )
    con.commit()
    con.close()

