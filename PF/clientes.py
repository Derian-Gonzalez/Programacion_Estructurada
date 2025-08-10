from conexionBD import conectar
from mysql.connector import Error
import datetime

def registrar_cliente(nombre, telefono, domicilio, ciudad, usuario_id):
    conexion = conectar()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        fecha = datetime.datetime.now()
        sql = """INSERT INTO clientes 
                (nombre, telefono, domicilio, ciudad, fecha_registro, registrado_por) 
                VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (nombre, telefono, domicilio, ciudad, fecha, usuario_id)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Error as err:
        print(f"Error al registrar cliente: {err}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def obtener_clientes():
    conexion = conectar()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        sql = """SELECT c.*, u.nombre as registrado_por_nombre 
                FROM clientes c 
                JOIN usuarios u ON c.registrado_por = u.id 
                ORDER BY c.nombre"""
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as err:
        print(f"Error al obtener clientes: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def buscar_clientes(criterio):
    conexion = conectar()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        sql = """SELECT * FROM clientes 
                WHERE nombre LIKE %s OR telefono LIKE %s OR ciudad LIKE %s"""
        val = (f"%{criterio}%", f"%{criterio}%", f"%{criterio}%")
        cursor.execute(sql, val)
        return cursor.fetchall()
    except Error as err:
        print(f"Error al buscar clientes: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def contar_clientes():
    conexion = conectar()
    if not conexion:
        return 0
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM clientes")
        return cursor.fetchone()[0]
    except Error as err:
        print(f"Error al contar clientes: {err}")
        return 0
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()