import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_paqueteria"
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None