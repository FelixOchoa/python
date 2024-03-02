from fastapi import FastAPI
from utils.data import estudiantes
from services.studentServices import addStudent
from config.database import cursor, conexion
## Añado CORS para poder controlar el acceso mediante Internet
from fastapi.middleware.cors import CORSMiddleware

## Origenes de los que se le permite enviar solicitudes
origins = [
    "http://localhost:5173",
]
app = FastAPI()

## Establecemos el middleware en la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/usuarios")
def get_users():
    usuarios = cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()

    usuariosParseadosAJSON = []

    for usuario in usuarios:
        usuarioJSON = {
            "id": usuario[0],
            "username": usuario[1],
            "password": usuario[2],
            "foto": usuario[3],
            "nombre": usuario[4],
            "correo": usuario[5],
            "telefono": usuario[6],
            "id_rol": usuario[7],
        }
        usuariosParseadosAJSON.append(usuarioJSON)

    return usuariosParseadosAJSON

@app.get("/usuarios/{username}")
def getUserByUsername(username: str):
    usuario = cursor.execute(f"SELECT * FROM usuario WHERE username = '{username}'")
    usuario = cursor.fetchone()

    if usuario:
        usuarioJSON = {
            "id": usuario[0],
            "username": usuario[1],
            "password": usuario[2],
            "foto": usuario[3],
            "nombre": usuario[4],
            "correo": usuario[5],
            "telefono": usuario[6],
            "id_rol": usuario[7],
        }
        return usuarioJSON
    else:
        return {"error": "Usuario no encontrado"}

@app.post("/usuarios")
def addUser(username: str, password: str, foto: str, nombre: str, correo: str, telefono: str, id_rol: int):
    cursor.execute(f"INSERT INTO usuario (username, password, foto, nombre, correo, telefono, idRol) VALUES ('{username}', '{password}', '{foto}', '{nombre}', '{correo}', '{telefono}', {id_rol})")
    conexion.commit()

    return {"message": "Usuario agregado"}

## Actualizar todo un objeto
# @app.put("/estudiantes/{estudiante_id}")
# def update_student(estudiante_id: int, nombre: str, edad: int, colegio: str, direccion: str, documento: str, tipo_documento: str):
#     for estudiante in estudiantes:
#         if estudiante["id"] == estudiante_id:
#             estudiante["nombre"] = nombre
#             estudiante["edad"] = edad
#             estudiante["colegio"] = colegio
#             estudiante["direccion"] = direccion
#             estudiante["documento"] = documento
#             estudiante["tipo_documento"] = tipo_documento
#             return {"message": "Estudiante actualizado"}
#     else:
#         return {"error": "Estudiante no encontrado"}

## Actualizar campo por campo
# @app.patch("/estudiantes/{estudiante_id}")
# def patch_student(estudiante_id: int, nombre: str = None, edad: int = None, colegio: str = None, direccion: str = None, documento: str = None, tipo_documento: str = None):
#     for estudiante in estudiantes:
#         if estudiante["id"] == estudiante_id:
#             if nombre:
#                 estudiante["nombre"] = nombre
#             if edad:
#                 estudiante["edad"] = edad
#             if colegio:
#                 estudiante["colegio"] = colegio
#             if direccion:
#                 estudiante["direccion"] = direccion
#             if documento:
#                 estudiante["documento"] = documento
#             if tipo_documento:
#                 estudiante["tipo_documento"] = tipo_documento
#             return {"message": "Estudiante actualizado"}
#     else:
#         return {"error": "Estudiante no encontrado"}

## Eliminar un objeto
# @app.delete("/estudiantes/{estudiante_id}")
# def delete_student(estudiante_id: int):
#     for estudiante in estudiantes:
#         if estudiante["id"] == estudiante_id:
#             estudiantes.remove(estudiante)
#             return {"message": "Estudiante eliminado"}
#     else:
#         return {"error": "Estudiante no encontrado"}