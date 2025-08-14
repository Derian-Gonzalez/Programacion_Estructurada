import os
from clientes import registrar_cliente, obtener_clientes, buscar_clientes, contar_clientes, eliminar_cliente
from envios import registrar_envio, obtener_envios, actualizar_estado_envio, contar_envios, calcular_ingresos_totales
from paquetes import generar_numero_guia
from autentication import verificar_login, registrar_usuario, obtener_usuarios_por_rol, eliminar_usuario
from exportaciones import exportar_envios_excel, exportar_clientes_excel
import datetime
import getpass

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_login():
    """Muestra la pantalla de inicio de sesión"""
    limpiar_pantalla()
    print(f"{'=== 📦 SISTEMA DE PAQUETERÍA 📦 ===':^60}")
    print(f"{'--- 🖥️📦INICIO DE SESIÓN ---':^60}")
    email = input("Email: ")
    password = getpass.getpass("Contraseña: ")
    return verificar_login(email, password)

def validar_telefono(telefono):
    """Valida que el teléfono solo contenga números y tenga máximo 10 dígitos"""
    if not telefono.isdigit():
        print("\nLo siento, en el teléfono solo se deben ingresar dígitos numéricos.")
        input("Presione Enter para intentar nuevamente...")
        limpiar_pantalla()
        return False
    if len(telefono) > 10:
        print("\nLo siento, el teléfono debe tener un máximo de 10 dígitos.")
        input("Presione Enter para intentar nuevamente...")
        limpiar_pantalla()
        return False
    return True

def validar_id(id_str):
    """Valida que el ID sea un número"""
    if not id_str.isdigit():
        print("\nError: El ID debe ser un número.")
        input("Presione Enter para continuar...")
        return False
    return True

def menu_principal(usuario):
    """Menú principal con opción de salir siempre disponible"""
    while True:
        limpiar_pantalla()
        print(f"\n{'===📋📌 MENÚ PRINCIPAL ===':^60}")
        print(f"{f"Usuario:👤🆕📝 {usuario['nombre']} ({usuario['rol']})":^60}")
        print(f"\n{'1. 👤🆕📝Gestión de Clientes':^60}")
        print(f"{'2. 📜👥Gestión de Envíos':^60}")
        print(f"{'3. 📦📋Reportes y Estadísticas':^60}")
        if usuario['rol'] == 'administrador':
            print(f"{'4.📜👥 Gestión de Usuarios':^60}")
        print(f"{'0. 👋🛑Salir del sistema':^60}")
        
        # Corrección: El mensaje se pasa directamente a input
        opcion = input("\nSeleccione una opción (0 para salir): ")
        input("\nPresione Enter para continuar...")
        
        if opcion == "0":
            return False
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
        print(f"\n{'===📜👥 GESTIÓN DE USUARIOS ===':^60}")
        print(f"{'1. 🔑👤Gestionar Secretarías':^60}")
        print(f"{'2.👤✍️ Gestionar Repartidores':^60}")
        print(f"{'0. 📋📌Volver al menú principal':^60}")
        
        # Corrección: El mensaje se pasa directamente a input
        opcion = input("\nSeleccione una opción (0 para volver): ")
        input("\nPresione Enter para continuar...")
        
        if opcion == "0":
            break
        elif opcion == "1":
            gestionar_usuarios_tipo(2, usuario)
        elif opcion == "2":
            gestionar_usuarios_tipo(3, usuario)
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def gestionar_usuarios_tipo(rol_id, usuario_admin):
    """Función para gestionar usuarios por tipo"""
    tipo_usuario = "secretarías" if rol_id == 2 else "repartidores"
    
    while True:
        limpiar_pantalla()
        print(f"\n{f'=== 📜👥GESTIÓN DE {tipo_usuario.upper()} ===':^60}")
        print(f"{'1. 👤🆕📝Registrar nuevo':^60}")
        print(f"{'2. 📄👥Listar todos':^60}")
        print(f"{'3.🗑️👤 Eliminar':^60}")
        print(f"{'0.📋📌 Volver al menú anterior':^60}")
        
        # Corrección: El mensaje se pasa directamente a input
        opcion = input("\nSeleccione una opción (0 para volver): ")
        input("\nPresione Enter para continuar...")
        
        if opcion == "0":
            break
        elif opcion == "1":
            registrar_nuevo_usuario(rol_id, usuario_admin)
        elif opcion == "2":
            listar_usuarios_por_rol(rol_id)
        elif opcion == "3":
            eliminar_usuario_por_rol(rol_id)
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def eliminar_usuario_por_rol(rol_id):
    """Función para eliminar usuarios por rol"""
    limpiar_pantalla()
    tipo = "SECRETARÍA" if rol_id == 2 else "REPARTIDOR"
    print(f"\n{'--- ELIMINAR ' + tipo + ' ---':^60}")
    
    listar_usuarios_por_rol(rol_id)
    
    # Corrección: El mensaje se pasa directamente a input
    usuario_id = input("\nIngrese el ID del usuario a eliminar (0 para cancelar): ")
    if usuario_id == "0":
        return
    
    if validar_id(usuario_id):
        # Corrección: El mensaje se pasa directamente a input
        confirmacion = input(f"\n¿Está seguro que desea eliminar al usuario con ID {usuario_id}? (s/n): ")
        if confirmacion.lower() == 's':
            if eliminar_usuario(usuario_id):
                input("\nUsuario eliminado exitosamente! Presione Enter para continuar...")
            else:
                input("\nError al eliminar usuario. Presione Enter para continuar...")

def registrar_nuevo_usuario(rol_id, usuario_admin):
    """Registra un nuevo usuario según su rol"""
    limpiar_pantalla()
    tipo = "SECRETARÍA" if rol_id == 2 else "REPARTIDOR"
    print(f"\n{'--- REGISTRAR NUEVO ' + tipo + ' ---':^60}")
    
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
    print(f"\n{'--- LISTA DE ' + tipo + ' ---':^60}")
    
    usuarios = obtener_usuarios_por_rol(rol_id)
    if not usuarios:
        print("No hay usuarios registrados en esta categoría")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']} {usuario['apellidos']} | Email: {usuario['email']}")
    
    input("\nPresione Enter para continuar...")

def menu_gestion_clientes(usuario):
    """📋📌Menú para gestión de clientes"""
    while True:
        limpiar_pantalla()
        print(f"\n{'=== GESTIÓN DE CLIENTES ===':^60}")
        print(f"{'1. 👤🆕📝Registrar nuevo cliente':^60}")
        print(f"{'2. 📜👥Listar todos los clientes':^60}")
        print(f"{'3. 🔍🗂️Buscar cliente':^60}")
        print(f"{'4. 🗑️👤Eliminar cliente':^60}")
        print(f"{'0. 📋📌Volver al menú principal':^60}")
        
        # Corrección: El mensaje se pasa directamente a input
        opcion = input("\nSeleccione una opción (0 para volver): ")
        input("\nPresione Enter para continuar...")
        
        if opcion == "0":
            break
        elif opcion == "1":
            registrar_nuevo_cliente(usuario)
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            eliminar_cliente_menu()
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def eliminar_cliente_menu():
    """Función para eliminar clientes"""
    limpiar_pantalla()
    print(f"\n{'--- ELIMINAR CLIENTE ---':^60}")
    
    listar_clientes()
    
    # Corrección: El mensaje se pasa directamente a input
    cliente_id = input("\nIngrese el ID del cliente a eliminar (0 para cancelar): ")
    if cliente_id == "0":
        return
    
    if validar_id(cliente_id):
        # Corrección: El mensaje se pasa directamente a input
        confirmacion = input(f"\n¿Está seguro que desea eliminar al cliente con ID {cliente_id}? (s/n): ")
        if confirmacion.lower() == 's':
            if eliminar_cliente(cliente_id):
                input("\nCliente eliminado exitosamente! Presione Enter para continuar...")
            else:
                input("\nError al eliminar cliente. Presione Enter para continuar...")

def registrar_nuevo_cliente(usuario):
    """Función para registrar nuevo cliente con validación de teléfono mejorada"""
    while True:
        limpiar_pantalla()
        print(f"\n{'--- REGISTRAR NUEVO CLIENTE ---':^60}")
        nombre = input("Nombre completo: ")
        
        telefono = ""
        while True:
            telefono = input("Teléfono: ")
            if validar_telefono(telefono):
                break
            
        domicilio = input("Domicilio: ")
        ciudad = input("Ciudad: ")
        
        if registrar_cliente(nombre, telefono, domicilio, ciudad, usuario['id']):
            input("\nCliente registrado exitosamente! Presione Enter para continuar...")
            break
        else:
            opcion = input("\nError al registrar cliente. ¿Desea intentar nuevamente? (s/n): ")
            if opcion.lower() != 's':
                break

def listar_clientes():
    """Función para listar clientes"""
    limpiar_pantalla()
    print(f"\n{'--- LISTADO DE CLIENTES ---':^60}")
    clientes = obtener_clientes()
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Nombre: {cliente['nombre']} | Tel: {cliente['telefono']} | Ciudad: {cliente['ciudad']}")
    input("\nPresione Enter para continuar...")

def buscar_cliente():
    """Función para buscar clientes"""
    limpiar_pantalla()
    print(f"\n{'--- BUSCAR CLIENTE ---':^60}")
    criterio = input("Ingrese nombre, teléfono o ciudad para buscar: ")
    resultados = buscar_clientes(criterio)
    
    if resultados:
        print(f"\n{'--- RESULTADOS DE BÚSQUEDA ---':^60}")
        for cliente in resultados:
            print(f"ID: {cliente['id']} | Nombre: {cliente['nombre']} | Tel: {cliente['telefono']}")
    else:
        print("No se encontraron coincidencias")
    
    input("\nPresione Enter para continuar...")

def menu_gestion_envios(usuario):
    """📋📌Menú para gestión de envíos"""
    while True:
        limpiar_pantalla()
        print(f"\n{'=== 👤✍️GESTIÓN DE ENVÍOS ===':^60}")
        print(f"{'1.👤🆕📝 Registrar nuevo envío':^60}")
        print(f"{'2. 📦📋Listar todos los envíos':^60}")
        print(f"{'3. 🔄🚚Actualizar estado de envío':^60}")
        print(f"{'0. 📋📌Volver al menú principal':^60}")
        
        # Corrección: El mensaje se pasa directamente a input
        opcion = input("\nSeleccione una opción (0 para volver): ")
        input("\nPresione Enter para continuar...")
        
        if opcion == "0":
            break
        elif opcion == "1":
            registrar_nuevo_envio(usuario)
        elif opcion == "2":
            listar_envios()
        elif opcion == "3":
            actualizar_estado_envio_mejorado()
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def actualizar_estado_envio_mejorado():
    """Función mejorada para actualizar estado de envío"""
    while True:
        limpiar_pantalla()
        print(f"\n{'--- ACTUALIZAR ESTADO DE ENVÍO ---':^60}")
        
        try:
            numero_guia = input("Número de guía: ").strip()
            if not numero_guia:
                print("Error: Debe ingresar un número de guía.")
                input("\nPresione Enter para continuar...")
                continue
            
            print("\nEstados disponibles:")
            print("1. Pendiente | 2. En proceso | 3. En camino | 4. Entregado")
            
            estado_id = input("Nuevo estado (1-4): ").strip()
            if not estado_id or estado_id not in ['1', '2', '3', '4']:
                print("Error: Debe seleccionar un estado válido (1-4).")
                input("\nPresione Enter para continuar...")
                continue
            
            repartidor_id = None
            repartidor_input = input("ID del repartidor (opcional, presione Enter para omitir): ").strip()
            if repartidor_input:
                if validar_id(repartidor_input):
                    repartidor_id = repartidor_input
                else:
                    print("\nAdvertencia: ID de repartidor no válido, se omitirá.")
                    input("Presione Enter para continuar...")
            
            if actualizar_estado_envio(numero_guia, estado_id, repartidor_id):
                input("\nEstado actualizado exitosamente! Presione Enter para continuar...")
                break
            else:
                opcion = input("\nError al actualizar estado. ¿Desea intentar nuevamente? (s/n): ")
                if opcion.lower() != 's':
                    break
                    
        except Exception as e:
            print(f"\nError inesperado: {str(e)}")
            input("Presione Enter para continuar...")
            continue

def registrar_nuevo_envio(usuario):
    """Función para registrar nuevo envío con validación de ID"""
    while True:
        limpiar_pantalla()
        print(f"\n{'--- REGISTRAR NUEVO ENVÍO ---':^60}")
        
        cliente_id = ""
        while True:
            cliente_id = input("ID del cliente: ")
            if validar_id(cliente_id):
                break
            
        descripcion = input("Descripción del paquete: ")
        peso = input("Peso (kg): ")
        dimensiones = input("Dimensiones (LxAxA): ")
        monto = input("Monto: ")
        
        repartidor_id = None
        repartidor_input = input("ID del repartidor (opcional, presione Enter para omitir): ")
        if repartidor_input:
            if validar_id(repartidor_input):
                repartidor_id = repartidor_input
            else:
                print("\nAdvertencia: ID de repartidor no válido, se omitirá.")
                input("Presione Enter para continuar...")
        
        numero_guia = registrar_envio(
            cliente_id, descripcion, peso, dimensiones, monto, 
            usuario['id'], repartidor_id
        )
        
        if numero_guia:
            input(f"\nEnvío registrado exitosamente! N° de guía: {numero_guia}\nPresione Enter para continuar...")
            break
        else:
            opcion = input("\nError al registrar envío. ¿Desea intentar nuevamente? (s/n): ")
            if opcion.lower() != 's':
                break

def listar_envios():
    """Función para listar envíos"""
    limpiar_pantalla()
    print(f"\n{'--- LISTADO DE ENVÍOS ---':^60}")
    envios = obtener_envios()
    for envio in envios:
        print(f"Guía: {envio['numero_guia']} | Cliente: {envio['cliente_nombre']} | Estado: {envio['estado']}")
    input("\nPresione Enter para continuar...")

def menu_reportes(usuario):
    """📋📌Menú para reportes y estadísticas"""
    while True:
        limpiar_pantalla()
        print(f"\n{'=== 📦📝REPORTES Y ESTADÍSTICAS ===':^60}")
        print(f"{'1. 📜👥Total de clientes registrados':^60}")
        print(f"{'2. 📬✅Total de envíos registrados':^60}")
        print(f"{'3. 🔍🗂️Ingresos totales por envíos entregados':^60}")
        print(f"{'4. 🗄️🗂️📊Exportar envíos a Excel':^60}")
        print(f"{'5. 🗄️🗂️📊Exportar clientes a Excel':^60}")
        print(f"{'0. 📋📌Volver al menú principal':^60}")
        
        # Corrección: El mensaje se pasa directamente a input
        opcion = input("\nSeleccione una opción (0 para volver): ")
        input("\nPresione Enter para continuar...")
        
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
        
        if menu_principal(usuario) is False:
            limpiar_pantalla()
            print("\n=== SESIÓN FINALIZADA ===")
            print("Gracias por usar el sistema de paquetería")
            break

if __name__ == "__main__":
    main()