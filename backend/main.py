from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

def init_db():
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    );
    """)
    con.commit()
    con.close()

class User(BaseModel):
    username: str
    password: str

init_db()

app = FastAPI()

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
async def register(user :User):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (user.username,))

    result = cursor.fetchone()

    if result:
        con.close()
        return {"message": "El usuario ya existe"}
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, user.password))
        con.commit()
        con.close()
        return {"message": "Usuario registrado exitosamente"}
