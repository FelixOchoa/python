from utils.data import estudiantes

def addStudent(id: int, nombre: str, edad: int, colegio: str, direccion: str, documento: str, tipo_documento: str):
    estudiantes.append({
        "id": id,
        "nombre": nombre,
        "edad": edad,
        "colegio": colegio,
        "direccion": direccion,
        "documento": documento,
        "tipo_documento": tipo_documento
    })
    return {"message": "Estudiante agregado"}