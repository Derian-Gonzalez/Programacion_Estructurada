import os
from clientes import registrar_cliente, obtener_clientes, buscar_clientes, contar_clientes
from envios import registrar_envio, obtener_envios, actualizar_estado_envio, contar_envios, calcular_ingresos_totales
from paquetes import generar_numero_guia
from autentication import verificar_login, registrar_usuario, obtener_usuarios_por_rol
from exportaciones import exportar_envios_excel, exportar_clientes_excel
import datetime
import getpass

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_login():
    """Muestra la pantalla de inicio de sesión"""
    limpiar_pantalla()
    print("\n=== SISTEMA DE PAQUETERÍA ===")
    
    print("--- INICIO DE SESIÓN ---")
    email = input("Email: ")
    password = getpass.getpass("Contraseña: ")
    return verificar_login(email, password)

def menu_principal(usuario):
    """Menú principal con opción de salir siempre disponible"""
    while True:
        limpiar_pantalla()
        print(f"\n=== MENÚ PRINCIPAL ===")
        print(f"Usuario: {usuario['nombre']} ({usuario['rol']})")
        print("\n1. Gestión de Clientes")
        print("2. Gestión de Envíos")
        print("3. Reportes y Estadísticas")
        if usuario['rol'] == 'administrador':
            print("4. Gestión de Usuarios")
        print("0. Salir del sistema")
        
        opcion = input("\nSeleccione una opción (0 para salir): ")
        
        if opcion == "0":
            return False  # Indicador para salir
        elif opcion == "1":
            menu_gestion_clientes(usuario)
        elif opcion == "2":
            menu_gestion_envios(usuario)
        elif opcion == "3":
            menu_reportes(usuario)
        elif opcion == "4" and usuario['rol'] == 'administrador':
            menu_gestion_usuarios(usuario)
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def menu_gestion_usuarios(usuario):
    """Menú para gestión de usuarios (solo admin)"""
    while True:
        limpiar_pantalla()
        print("\n=== GESTIÓN DE USUARIOS ===")
        print("1. Gestionar Secretarías")
        print("2. Gestionar Repartidores")
        print("0. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción (0 para volver): ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            gestionar_usuarios_tipo(2, usuario)  # 2 = Rol de secretaria
        elif opcion == "2":
            gestionar_usuarios_tipo(3, usuario)  # 3 = Rol de repartidor
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def gestionar_usuarios_tipo(rol_id, usuario_admin):
    """Función para gestionar usuarios por tipo (secretarias o repartidores)"""
    tipo_usuario = "secretarías" if rol_id == 2 else "repartidores"
    
    while True:
        limpiar_pantalla()
        print(f"\n=== GESTIÓN DE {tipo_usuario.upper()} ===")
        print("1. Registrar nuevo")
        print("2. Listar todos")
        print("0. Volver al menú anterior")
        
        opcion = input("\nSeleccione una opción (0 para volver): ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            registrar_nuevo_usuario(rol_id, usuario_admin)
        elif opcion == "2":
            listar_usuarios_por_rol(rol_id)
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def registrar_nuevo_usuario(rol_id, usuario_admin):
    """Registra un nuevo usuario según su rol"""
    limpiar_pantalla()
    tipo = "SECRETARÍA" if rol_id == 2 else "REPARTIDOR"
    print(f"\n--- REGISTRAR NUEVO {tipo} ---")
    
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    email = input("Email: ")
    password = getpass.getpass("Contraseña: ")
    
    if registrar_usuario(nombre, apellidos, email, password, rol_id, usuario_admin['id']):
        input("\nUsuario registrado exitosamente! Presione Enter para continuar...")
    else:
        input("\nError al registrar usuario. Presione Enter para continuar...")

def listar_usuarios_por_rol(rol_id):
    """Lista usuarios según su rol"""
    limpiar_pantalla()
    tipo = "SECRETARÍAS" if rol_id == 2 else "REPARTIDORES"
    print(f"\n--- LISTA DE {tipo} ---")
    
    usuarios = obtener_usuarios_por_rol(rol_id)
    if not usuarios:
        print("No hay usuarios registrados en esta categoría")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']} {usuario['apellidos']} | Email: {usuario['email']}")
    
    input("\nPresione Enter para continuar...")

def menu_gestion_clientes(usuario):
    """Menú para gestión de clientes"""
    while True:
        limpiar_pantalla()
        print("\n=== GESTIÓN DE CLIENTES ===")
        print("1. Registrar nuevo cliente")
        print("2. Listar todos los clientes")
        print("3. Buscar cliente")
        print("0. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción (0 para volver): ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            registrar_nuevo_cliente(usuario)
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def registrar_nuevo_cliente(usuario):
    """Función para registrar nuevo cliente"""
    limpiar_pantalla()
    print("\n--- REGISTRAR NUEVO CLIENTE ---")
    nombre = input("Nombre completo: ")
    telefono = input("Teléfono: ")
    domicilio = input("Domicilio: ")
    ciudad = input("Ciudad: ")
    
    if registrar_cliente(nombre, telefono, domicilio, ciudad, usuario['id']):
        input("\nCliente registrado exitosamente! Presione Enter para continuar...")
    else:
        input("\nError al registrar cliente. Presione Enter para continuar...")

def listar_clientes():
    """Función para listar clientes"""
    limpiar_pantalla()
    print("\n--- LISTADO DE CLIENTES ---")
    clientes = obtener_clientes()
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Nombre: {cliente['nombre']} | Tel: {cliente['telefono']} | Ciudad: {cliente['ciudad']}")
    input("\nPresione Enter para continuar...")

def buscar_cliente():
    """Función para buscar clientes"""
    limpiar_pantalla()
    print("\n--- BUSCAR CLIENTE ---")
    criterio = input("Ingrese nombre, teléfono o ciudad para buscar: ")
    resultados = buscar_clientes(criterio)
    
    if resultados:
        print("\n--- RESULTADOS DE BÚSQUEDA ---")
        for cliente in resultados:
            print(f"ID: {cliente['id']} | Nombre: {cliente['nombre']} | Tel: {cliente['telefono']}")
    else:
        print("No se encontraron coincidencias")
    
    input("\nPresione Enter para continuar...")

def menu_gestion_envios(usuario):
    """Menú para gestión de envíos"""
    while True:
        limpiar_pantalla()
        print("\n=== GESTIÓN DE ENVÍOS ===")
        print("1. Registrar nuevo envío")
        print("2. Listar todos los envíos")
        print("3. Actualizar estado de envío")
        print("0. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción (0 para volver): ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            registrar_nuevo_envio(usuario)
        elif opcion == "2":
            listar_envios()
        elif opcion == "3":
            actualizar_estado_envio()
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def registrar_nuevo_envio(usuario):
    """Función para registrar nuevo envío"""
    limpiar_pantalla()
    print("\n--- REGISTRAR NUEVO ENVÍO ---")
    
    cliente_id = input("ID del cliente: ")
    descripcion = input("Descripción del paquete: ")
    peso = input("Peso (kg): ")
    dimensiones = input("Dimensiones (LxAxA): ")
    monto = input("Monto: ")
    repartidor_id = input("ID del repartidor (opcional): ") or None
    
    numero_guia = registrar_envio(
        cliente_id, descripcion, peso, dimensiones, monto, 
        usuario['id'], repartidor_id
    )
    
    if numero_guia:
        input(f"\nEnvío registrado exitosamente! N° de guía: {numero_guia}\nPresione Enter para continuar...")
    else:
        input("\nError al registrar envío. Presione Enter para continuar...")

def listar_envios():
    """Función para listar envíos"""
    limpiar_pantalla()
    print("\n--- LISTADO DE ENVÍOS ---")
    envios = obtener_envios()
    for envio in envios:
        print(f"Guía: {envio['numero_guia']} | Cliente: {envio['cliente_nombre']} | Estado: {envio['estado']}")
    input("\nPresione Enter para continuar...")

def actualizar_estado_envio():
    """Función para actualizar estado de envío"""
    limpiar_pantalla()
    print("\n--- ACTUALIZAR ESTADO DE ENVÍO ---")
    numero_guia = input("Número de guía: ")
    print("\nEstados disponibles:")
    print("1. Pendiente | 2. En proceso | 3. En camino | 4. Entregado")
    estado_id = input("Nuevo estado (1-4): ")
    repartidor_id = input("ID del repartidor (opcional): ") or None
    
    if actualizar_estado_envio(numero_guia, estado_id, repartidor_id):
        input("\nEstado actualizado exitosamente! Presione Enter para continuar...")
    else:
        input("\nError al actualizar estado. Presione Enter para continuar...")

def menu_reportes(usuario):
    """Menú para reportes y estadísticas"""
    while True:
        limpiar_pantalla()
        print("\n=== REPORTES Y ESTADÍSTICAS ===")
        print("1. Total de clientes registrados")
        print("2. Total de envíos registrados")
        print("3. Ingresos totales por envíos entregados")
        print("4. Exportar envíos a Excel")
        print("5. Exportar clientes a Excel")
        print("0. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción (0 para volver): ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            mostrar_total_clientes()
        elif opcion == "2":
            mostrar_total_envios()
        elif opcion == "3":
            mostrar_ingresos_totales()
        elif opcion == "4":
            exportar_envios_excel()
            input("\nPresione Enter para continuar...")
        elif opcion == "5":
            exportar_clientes_excel()
            input("\nPresione Enter para continuar...")
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def mostrar_total_clientes():
    """Muestra el total de clientes registrados"""
    limpiar_pantalla()
    total = contar_clientes()
    print(f"\nTotal de clientes registrados: {total}")
    input("\nPresione Enter para continuar...")

def mostrar_total_envios():
    """Muestra el total de envíos registrados"""
    limpiar_pantalla()
    total = contar_envios()
    print(f"\nTotal de envíos registrados: {total}")
    input("\nPresione Enter para continuar...")

def mostrar_ingresos_totales():
    """Muestra los ingresos totales por envíos entregados"""
    limpiar_pantalla()
    ingresos = calcular_ingresos_totales()
    print(f"\nIngresos totales por envíos entregados: ${ingresos:.2f}")
    input("\nPresione Enter para continuar...")

def main():
    """Función principal del programa"""
    while True:
        usuario = mostrar_login()
        if not usuario:
            input("\nCredenciales incorrectas. Presione Enter para continuar...")
            continue
        
        # Bucle principal con opción de salir
        if menu_principal(usuario) is False:
            limpiar_pantalla()
            print("\n=== SESIÓN FINALIZADA ===")
            print("Gracias por usar el sistema de paquetería")
            break

if __name__ == "__main__":
    main()