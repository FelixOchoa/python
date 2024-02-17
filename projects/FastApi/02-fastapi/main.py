from fastapi import FastAPI
from utils.data import estudiantes
from services.studentServices import addStudent

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/estudiantes")
def get_students():
    return estudiantes

@app.get("/estudiantes/{estudiante_id}")
def get_student(estudiante_id: int):
    for estudiante in estudiantes:
         if estudiante["id"] == estudiante_id:
             return estudiante
    else:
         return {"error": "Estudiante no encontrado"}

@app.post("/estudiantes")
def add_student(id: int, nombre: str, edad: int, colegio: str, direccion: str, documento: str, tipo_documento: str):
    return addStudent(id, nombre, edad, colegio, direccion, documento, tipo_documento)

@app.put("/estudiantes/{estudiante_id}")
def update_student(estudiante_id: int, nombre: str, edad: int, colegio: str, direccion: str, documento: str, tipo_documento: str):
    for estudiante in estudiantes:
        if estudiante["id"] == estudiante_id:
            estudiante["nombre"] = nombre
            estudiante["edad"] = edad
            estudiante["colegio"] = colegio
            estudiante["direccion"] = direccion
            estudiante["documento"] = documento
            estudiante["tipo_documento"] = tipo_documento
            return {"message": "Estudiante actualizado"}
    else:
        return {"error": "Estudiante no encontrado"}
    
@app.patch("/estudiantes/{estudiante_id}")
def patch_student(estudiante_id: int, nombre: str = None, edad: int = None, colegio: str = None, direccion: str = None, documento: str = None, tipo_documento: str = None):
    for estudiante in estudiantes:
        if estudiante["id"] == estudiante_id:
            if nombre:
                estudiante["nombre"] = nombre
            if edad:
                estudiante["edad"] = edad
            if colegio:
                estudiante["colegio"] = colegio
            if direccion:
                estudiante["direccion"] = direccion
            if documento:
                estudiante["documento"] = documento
            if tipo_documento:
                estudiante["tipo_documento"] = tipo_documento
            return {"message": "Estudiante actualizado"}
    else:
        return {"error": "Estudiante no encontrado"}

@app.delete("/estudiantes/{estudiante_id}")
def delete_student(estudiante_id: int):
    for estudiante in estudiantes:
        if estudiante["id"] == estudiante_id:
            estudiantes.remove(estudiante)
            return {"message": "Estudiante eliminado"}
    else:
        return {"error": "Estudiante no encontrado"}