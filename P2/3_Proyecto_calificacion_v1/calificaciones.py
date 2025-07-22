def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t... Oprima cualquier tecla para continuar...")


 
def menu_principal():
    print("\n\t\t\t..::::: 📚 Sistema de Gestión de Calificaciones 📊 :::::...\n")
    print("\t\t1️⃣ -- Agregar calificaciones")
    print("\t\t2️⃣ -- Mostrar calificaciones")
    print("\t\t3️⃣ -- Calcular promedio")
    print("\t\t4️⃣ -- ❌ SALIR")
    opcion = input("\n\t\t🔹 Elige una opción (1-4): ").upper()
    return opcion

def agregar_calificaciones(Lista):
    borrarPantalla()
    print("📝 Agregar calificaciones")
    nombre = input("👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        continua = True
        while continua:
            try:
                cal = float(input(f"📌 Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("⚠️ Ingrese un valor entre 0 y 10")
            except ValueError:
                print("❗ Ingrese un valor numérico")
    Lista.append([nombre] + calificaciones)
    print("✅ Acción realizada con éxito")

def mostrar_calificaciones(Lista):
    borrarPantalla()
    print("📋 Mostrar calificaciones")
    if len(Lista) > 0:
        print(f"{'👨‍🎓 Nombre':<15}   {'📘 Calif1':<10}   {'📙 Calif2':<10}   {'📗 Calif3':<10}")
        print("-" * 50)
        for fila in Lista:
            print(f"{fila[0]:<15}   {fila[1]:<10}   {fila[2]:<10}   {fila[3]:<10}")
            print("-" * 50)
        print(f"👥 SON {len(Lista)} alumnos")
    else:
        print("🚫 No hay calificaciones en el sistema")

def calcular_calificaciones(lista):
    borrarPantalla()
    print("📈 Promedios de Alumnos")
    promedio_clase = 0
    alumnos = 0
    if len(lista) > 0:
        print(f"{'👨‍🎓 Nombre':<15}{'📊 Promedio':<10}")
        print("-" * 30)
        for fila in lista:
            promedios = (fila[1] + fila[2] + fila[3]) / 3
            print(f"{fila[0]:<15}{promedios:<10.2f}")
            promedio_clase += promedios
            alumnos += 1
        print("-" * 30)
        print(f"📌 Son {len(lista)} alumnos y tienen un promedio general de: {promedio_clase / alumnos:.2f}")
    else:
        print("🚫 No hay calificaciones en el sistema")