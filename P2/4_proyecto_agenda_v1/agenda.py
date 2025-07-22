def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t... Oprima cualquier tecla para continuar...")

def menu_principal():
    print("\n\t\t..::::: 📇 Sistema de Gestión de Agenda de Contactos 📇 :::::...\n")
    print("\t\t\t1️⃣ -- Agregar Contacto")
    print("\t\t\t2️⃣ -- Mostrar Todos los Contactos")
    print("\t\t\t3️⃣ -- Buscar Contactos por Nombre")
    print("\t\t\t4️⃣ -- Eliminar Contacto")
    print("\t\t\t5️⃣ -- Modificar Contacto")
    print("\t\t\t6️⃣ -- Salir")
    opcion = input("\n\t\t🔹 Elige una opción (1-6): ").upper()
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t.:: ➕ Agregar Contacto ::.\n")
    nombre = input("Nombre del contacto: ").strip().title()
    telefono = input("Número de teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()
    domicilio = input("Domicilio: ").strip().title()
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
        "domicilio": domicilio
    }
    agenda.append(contacto)
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def buscar_nombre(agenda):
    borrarPantalla()
    print("\n\t.:: 🔍 Buscar Contacto por Nombre ::.\n")
    nombre_buscado = input("Ingresa el nombre a buscar: ").strip().title()
    encontrados = [c for c in agenda if c["nombre"] == nombre_buscado]
    if encontrados:
        for contacto in encontrados:
            print(f"\n\t📇 {contacto['nombre']} - 📞 {contacto['telefono']}")
    else:
        print("\n\t❗ No se encontró ningún contacto con ese nombre.")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n\t.:: 🗑️ Eliminar Contacto ::.\n")
    nombre = input("Ingresa el nombre del contacto a eliminar: ").strip().title()
    eliminado = False
    for contacto in agenda[:]:
        if contacto["nombre"] == nombre:
            agenda.remove(contacto)
            eliminado = True
    if eliminado:
        print("\n\t\t::: ¡Contacto eliminado exitosamente! :::")
    else:
        print("\n\t❗ No se encontró el contacto.")


def mostrar_contacto(agenda):
    borrarPantalla()
    print("\n\t.:: 📋 Lista de Contactos ::.\n")
    if not agenda:
        print("\tNo hay contactos registrados.")
    else:
        for i, contacto in enumerate(agenda, 1):
            print(f"\n\t{i}. 📇 Nombre: {contacto['nombre']}")
            print(f"\t   📞 Teléfono: {contacto['telefono']}")
            print(f"\t   📧 Correo: {contacto['correo']}")
            print(f"\t   🏠 Domicilio: {contacto['domicilio']}")


def modificar_contacto(agenda):
    borrarPantalla()
    print("\n\t.:: ✏️ Modificar Contacto ::.\n")
    nombre = input("Ingresa el nombre del contacto que deseas modificar: ").strip().title()
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            print(f"\n\t📇 Contacto encontrado:")
            print(f"\t   Nombre actual: {contacto['nombre']}")
            print(f"\t   Teléfono actual: {contacto['telefono']}")
            print(f"\t   Correo actual: {contacto['correo']}")
            print(f"\t   Domicilio actual: {contacto['domicilio']}")
            nuevo_nombre = input("\nNuevo nombre (deja vacío para mantener el actual): ").strip().title()
            nuevo_telefono = input("Nuevo teléfono (deja vacío para mantener el actual): ").strip()
            nuevo_correo = input("Nuevo correo electrónico (deja vacío para mantener el actual): ").strip()
            nuevo_domicilio = input("Nuevo domicilio (deja vacío para mantener el actual): ").strip().title()
            if nuevo_nombre:
                contacto["nombre"] = nuevo_nombre
            if nuevo_telefono:
                contacto["telefono"] = nuevo_telefono
            if nuevo_correo:
                contacto["correo"] = nuevo_correo
            if nuevo_domicilio:
                contacto["domicilio"] = nuevo_domicilio
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
            return
    print("\n\t❗ No se encontró el contacto con ese nombre.")

"""def eliminar_contacto(agenda):
    borrarPantalla()
    print("🗑️ Eliminar Contactos 🗑️")
    if not agenda:
        print("📭 No hay contactos en la Agenda")
    else:
        nombre = input("🔎 Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print("📋 Valores Actuales")
            print(f"👤 Nombre: {nombre}\n📞 Teléfono: {agenda[nombre][0]}\n📧 E-mail: {agenda[nombre][1]}")
            resp = input("❓¿Deseas eliminar los valores? (Sí/No) ").lower().strip()
            if resp == "si":
                agenda.pop(nombre)
                print("✅ Acción Realizada con éxito")
        else:
            print("⚠️ Este contacto no existe")"""



"""def modificar_contacto(agenda):
    borrarPantalla()
    print("🛠️ Modificar Contactos 🛠️")
    if not agenda:
        print("📭 No hay contactos en la Agenda")
    else:
        nombre = input("🔎 Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print("📋 Valores Actuales")
            print(f"👤 Nombre: {nombre}\n📞 Teléfono: {agenda[nombre][0]}\n📧 E-mail: {agenda[nombre][1]}")
            resp = input("❓¿Deseas cambiar los valores? (Sí/No) ").lower().strip()
            if resp == "si":
                tel = input("📞 Nuevo Teléfono: ").upper().strip()
                email = input("📧 Nuevo E-mail: ").lower().strip()
                agenda[nombre] = [tel, email]
                print("✅ Acción Realizada con éxito")
        else:
            print("⚠️ Este contacto no existe")"""

