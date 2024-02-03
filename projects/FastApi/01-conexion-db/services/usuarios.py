

def getUsers(cursor):
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    usuariosDict = []

    for usuario in usuarios:
        usuarioDict = {
            "nombre": usuario[0],
            "id": usuario[1],
            "edad": usuario[2],
            "direccion": usuario[3],
            "username": usuario[4],
            "password": usuario[5]
        }
        usuariosDict.append(usuarioDict)

    return usuariosDict

def generateTableHTML(usuarios):
    tableHTML = "<main style='padding: 20px; background-color: blue;'>"
    tableHTML += "<h1 style='text-align: center; color: white'>Usuarios</h1>"
    tableHTML += "<table style='border-collapse: collapse; width: 100%;'>"
    tableHTML += "<tr><th style='border: 1px solid black; padding: 8px;'>Nombre</th><th style='border: 1px solid black; padding: 8px;'>ID</th><th style='border: 1px solid black; padding: 8px;'>Edad</th><th style='border: 1px solid black; padding: 8px;'>Dirección</th><th style='border: 1px solid black; padding: 8px;'>Username</th><th style='border: 1px solid black; padding: 8px;'>Password</th></tr>"

    for usuario in usuarios:
        tableHTML += "<tr>"
        tableHTML += f"<td style='border: 1px solid white; padding: 8px; color: white;'>{usuario['nombre']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px; color: white;'>{usuario['id']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{usuario['edad']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{usuario['direccion']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{usuario['username']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{usuario['password']}</td>"
        tableHTML += "</tr>"

    tableHTML += "</table>"
    tableHTML += "<p> Esta información está sacada del curso de FastAPI </p>"
    tableHTML += "</main>"
    return tableHTML

def getUsersById(cursor, id: int):
    cursor.execute("SELECT * FROM usuarios WHERE id = '"+str(id)+"'")
    usuarioById = cursor.fetchall()

    newUser = {}

    for usuario in usuarioById:
        newUser = {
            "nombre": usuario[0],
            "id": usuario[1],
            "edad": usuario[2],
            "direccion": usuario[3],
            "username": usuario[4],
            "password": usuario[5]
        }

    return newUser

def createUser(cursor, conexion , nombre: str, edad: int, username: str, password: str, direccion: str):
    cursor.execute("INSERT INTO usuarios (Nombre, Edad, Direccion, username, password) VALUES ('"+nombre+"', '"+str(edad)+"', '"+direccion+"', '"+username+"', '"+password+"' )")
    conexion.commit()

    nuevosUsers = getUsers(cursor)
    return {"listaDeUsuarios": nuevosUsers}

def updateUser(cursor, conexion, name: str, newName: str):
    cursor.execute("UPDATE usuarios SET nombre = '"+newName+"' WHERE nombre = '"+str(name)+"'")
    conexion.commit()
    return {"mensaje": "Usuario actualizado correctamente"}