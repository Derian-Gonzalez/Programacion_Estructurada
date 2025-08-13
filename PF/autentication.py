from conexionBD import conectar
from mysql.connector import Error
import hashlib
import datetime
def hash_password(password):
    """Encripta la contraseña usando SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verificar_login(email, password):
    """Verifica las credenciales del usuario"""
    conexion = conectar()
    if not conexion:
        return None
    
    try:
        cursor = conexion.cursor(dictionary=True)
        sql = """SELECT u.id, u.nombre, u.apellidos, u.email, r.nombre as rol 
                FROM usuarios u 
                JOIN roles r ON u.rol_id = r.id 
                WHERE u.email = %s AND u.password = %s"""
        val = (email, hash_password(password))
        cursor.execute(sql, val)
        usuario = cursor.fetchone()
        return usuario
    except Error as err:
        print(f"Error al verificar login: {err}")
        return None
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def registrar_usuario(nombre, apellidos, email, password, rol_id, usuario_admin_id):
    """Registra un nuevo usuario (solo administrador)"""
    conexion = conectar()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        fecha = datetime.datetime.now()
        sql = """INSERT INTO usuarios 
                (nombre, apellidos, email, password, rol_id, fecha_registro) 
                VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (nombre, apellidos, email, hash_password(password), rol_id, fecha)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Error as err:
        print(f"Error al registrar usuario: {err}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def obtener_usuarios_por_rol(rol_id):
    """Obtiene usuarios por tipo de rol"""
    conexion = conectar()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        sql = """SELECT id, nombre, apellidos, email 
                FROM usuarios WHERE rol_id = %s"""
        cursor.execute(sql, (rol_id,))
        return cursor.fetchall()
    except Error as err:
        print(f"Error al obtener usuarios: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()