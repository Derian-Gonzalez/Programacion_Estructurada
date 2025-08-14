from conexionBD import conectar
from mysql.connector import Error
import datetime
from paquetes import generar_numero_guia

def obtener_envios_repartidor(repartidor_id, estados=None):
    conexion = conectar()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        if estados:
            placeholders = ', '.join(['%s'] * len(estados))
            sql = f"""SELECT e.*, c.nombre as cliente_nombre, c.domicilio 
                    FROM envios e
                    JOIN clientes c ON e.cliente_id = c.id
                    WHERE e.repartidor_id = %s AND e.estado_id IN ({placeholders})"""
            cursor.execute(sql, [repartidor_id] + estados)
        else:
            sql = """SELECT e.*, c.nombre as cliente_nombre, c.domicilio 
                    FROM envios e
                    JOIN clientes c ON e.cliente_id = c.id
                    WHERE e.repartidor_id = %s"""
            cursor.execute(sql, (repartidor_id,))
        return cursor.fetchall()
    except Error as err:
        print(f"Error al obtener envíos: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

            
def registrar_envio(cliente_id, descripcion, peso, dimensiones, monto, usuario_id, repartidor_id=None):
    conexion = conectar()
    if not conexion:
        return None
    
    try:
        cursor = conexion.cursor()
        numero_guia = generar_numero_guia()
        fecha = datetime.datetime.now()
        sql = """INSERT INTO envios 
                (numero_guia, cliente_id, descripcion, peso, dimensiones, monto, 
                estado_id, fecha_registro, repartidor_id, registrado_por) 
                VALUES (%s, %s, %s, %s, %s, %s, 1, %s, %s, %s)"""
        val = (numero_guia, cliente_id, descripcion, peso, dimensiones, monto, 
              fecha, repartidor_id, usuario_id)
        cursor.execute(sql, val)
        conexion.commit()
        return numero_guia
    except Error as err:
        print(f"Error al registrar envío: {err}")
        return None
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def obtener_envios():
    conexion = conectar()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        sql = """SELECT e.*, c.nombre as cliente_nombre, c.telefono, c.domicilio, c.ciudad,
                es.nombre as estado, u.nombre as repartidor_nombre
                FROM envios e
                JOIN clientes c ON e.cliente_id = c.id
                JOIN estados_envio es ON e.estado_id = es.id
                LEFT JOIN usuarios u ON e.repartidor_id = u.id
                ORDER BY e.fecha_registro DESC"""
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as err:
        print(f"Error al obtener envíos: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def obtener_envios_por_estado(estados):
    conexion = conectar()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        placeholders = ', '.join(['%s'] * len(estados))
        sql = f"""SELECT e.*, c.nombre as cliente_nombre 
                FROM envios e
                JOIN clientes c ON e.cliente_id = c.id
                WHERE e.estado_id IN ({placeholders})"""
        cursor.execute(sql, estados)
        return cursor.fetchall()
    except Error as err:
        print(f"Error al obtener envíos: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def obtener_envios_repartidor(repartidor_id, estados=None):
    conexion = conectar()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        if estados:
            placeholders = ', '.join(['%s'] * len(estados))
            sql = f"""SELECT e.*, c.nombre as cliente_nombre, c.domicilio 
                    FROM envios e
                    JOIN clientes c ON e.cliente_id = c.id
                    WHERE e.repartidor_id = %s AND e.estado_id IN ({placeholders})"""
            cursor.execute(sql, [repartidor_id] + estados)
        else:
            sql = """SELECT e.*, c.nombre as cliente_nombre, c.domicilio 
                    FROM envios e
                    JOIN clientes c ON e.cliente_id = c.id
                    WHERE e.repartidor_id = %s"""
            cursor.execute(sql, (repartidor_id,))
        return cursor.fetchall()
    except Error as err:
        print(f"Error al obtener envíos: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def actualizar_estado_envio(numero_guia, estado_id, repartidor_id=None):
    conexion = conectar()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        if estado_id == 4:  # Entregado
            sql = """UPDATE envios 
                    SET estado_id = %s, fecha_entrega = NOW(), repartidor_id = %s 
                    WHERE numero_guia = %s"""
            val = (estado_id, repartidor_id, numero_guia)
        else:
            sql = """UPDATE envios 
                    SET estado_id = %s, repartidor_id = %s 
                    WHERE numero_guia = %s"""
            val = (estado_id, repartidor_id, numero_guia)
        
        cursor.execute(sql, val)
        conexion.commit()
        return cursor.rowcount > 0
    except Error as err:
        print(f"Error al actualizar envío: {err}")
        return False
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def contar_envios():
    conexion = conectar()
    if not conexion:
        return 0
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM envios")
        return cursor.fetchone()[0]
    except Error as err:
        print(f"Error al contar envíos: {err}")
        return 0
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def contar_envios_por_estado(estado_id):
    conexion = conectar()
    if not conexion:
        return 0
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM envios WHERE estado_id = %s", (estado_id,))
        return cursor.fetchone()[0]
    except Error as err:
        print(f"Error al contar envíos: {err}")
        return 0
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def calcular_ingresos_totales():
    conexion = conectar()
    if not conexion:
        return 0.0
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT SUM(monto) FROM envios WHERE estado_id = 4")  # Solo entregados
        return cursor.fetchone()[0] or 0.0
    except Error as err:
        print(f"Error al calcular ingresos: {err}")
        return 0.0
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def obtener_contador_envios_por_estado():
    conexion = conectar()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        sql = """SELECT es.nombre, COUNT(e.id) as total
                FROM estados_envio es
                LEFT JOIN envios e ON es.id = e.estado_id
                GROUP BY es.id"""
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as err:
        print(f"Error al obtener contador: {err}")
        return []
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()