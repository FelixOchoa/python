from config.db import cursor, conexion
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/usuarios")
async def obtener_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    return usuarios
@app.post("/crear-usuario")
async def crear_usuario(nombre: str):
    cursor.execute("INSERT INTO usuarios (nombre) VALUES ('"+nombre+"')")
    conexion.commit()
    return {"mensaje": "Usuario creado correctamente"}

@app.put("/actualizar-usuario/{name}")
async def actualizar_usuario(name: str, newName: str):
    cursor.execute("UPDATE usuarios SET nombre = '"+newName+"' WHERE nombre = '"+str(name)+"'")
    conexion.commit()
    return {"mensaje": "Usuario actualizado correctamente"}
