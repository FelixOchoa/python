import mysql.connector

config = {
    "user": "root",
    "password": "12345",
    "host": "localhost",
    "port": "3307",
    "database": "dbrest"
}

conexion = mysql.connector.connect(
    user=config["user"],
    host=config["host"],
    password=config["password"],
    database=config["database"],
    port=config["port"]
)

cursor = conexion.cursor()

print(conexion)
