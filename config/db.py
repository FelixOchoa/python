import mysql.connector

conexion = mysql.connector.connect(
    user="root",
    host="localhost",
    password="123456789",
    database="curso-python",
    port="3306"
)

cursor = conexion.cursor()

print(conexion)


