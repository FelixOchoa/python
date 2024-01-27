import mysql.connector

conexion = mysql.connector.connect(
    user="root",
    host="localhost",
    password="2882",
    database="test",
    port="3306"
)

cursor = conexion.cursor()

print(conexion)


