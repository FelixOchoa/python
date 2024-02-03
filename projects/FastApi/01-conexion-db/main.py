from config.db import cursor, conexion
from services.usuarios import getUsers, generateTableHTML, getUsersById, createUser, updateUser
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/usuarios", response_class=HTMLResponse)
async def obtener_usuarios():
    users = getUsers(cursor)
    return generateTableHTML(users)


@app.get("/usuarios/{id}")
async def obtener_usuarios(id: int):
    resultadoUsuario = getUsersById(cursor, id)
    return resultadoUsuario

@app.post("/crear-usuario")
async def crear_usuario(nombre: str, edad: int, username: str, password: str, direccion: str):
    return createUser(cursor, conexion, nombre, edad, username, password, direccion)

@app.put("/actualizar-usuario/{name}")
async def actualizar_usuario(name: str, newName: str):
    return updateUser(cursor, conexion, name, newName)
