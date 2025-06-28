def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t... Oprima cualquier tecla para continuar...")

def menu_principal():
    print("\n\t\t\t..::::: Sistema de Gestión de calificaciones.:::...\n\n\t\t-1.--Agregar--\n\t\t-2.--Mostrar--\n\t\t-3.--calcular promedio --\n\t\t-4.--SALIR--")
    opcion = input("\n\t\t Elige una opción (1-4): ").upper()
    return opcion
    
def agregar_calificaciones(Lista):
    borrarPantalla
    print("Agregar calificaciones")
    nombre=input("Nombre del alumno").upper().strip()
    calificaciones=[]
    for i in range(1,4):
       continua=True
       while continua:
        try:
            cal=float(input(f"Calificacion {i}:"))
            if cal>=0 and cal<=10:
                calificaciones.append(cal)
                bandera=False
            else:
                print("Ingrese un valor comprendido entre el 0 y 10")
        except ValueError:
            print("Ingrese un valor numerico")
    Lista.append([nombre]+calificaciones)
    print("Accion realzada con exito")


def mostrar_calificaciones(Lista):
   borrarPantalla()
   print("Mostrar calificaciones")
   if len(Lista)>0:
       print(f"{'Nombre':<15}   {'Calif1':<10}   {'calif2':<10}   {'calif3':<10} ")
       print("-"*50)
       for fila in Lista:
           print(f"{fila[0]:<15}   {fila[1]:<10}   {fila[2]:<10}   {fila[3]:<10}")
           print("-"*50)
           print(f"SON {len(Lista)} alumnos")
   else:
       print("No hay calificaciones en el sistema")



"""def calcular_promedios(Lista):
    if not Lista:
        print("\n\t\tNo hay calificaciones registradas.")
        return
    print("\n\t\tPromedios de calificaciones:")
    for alumno in Lista:
        nombre = alumno[0]
        calificaciones = alumno[1:]
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"\n\t\tNombre: {nombre}, Promedio: {promedio:.2f}")"""


def calcular_calificaciones(lista):
    borrarPantalla()
    print("Promedios de Alumnos")
    promedio_clase=0
    alumnos=0
    if len(lista)>0:
        print(f"{"Nombre" :<15}{"Promedio":<10}")
        print("-"*30)
        for fila in lista:
         promedios=((fila[1])+(fila[2])+(fila[3]))/3
         print(f"{fila[0]:<15}{promedios:<10}")
         promedio_clase+=promedios
         alumnos+=1
        print("-"*30)
        print(f"Son {len(lista)} alumnos y tienen un promedio de {promedio_clase/alumnos}")
    else:
        print("No hay calificaiones en el sistema")