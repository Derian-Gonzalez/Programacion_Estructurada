"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento"""
  # 1.- Funcion que no recibe parametros y no regresa valor
def solicitardatos1():
    nombre=input("nombre:")
    telefono=input("telefono:")
    print(f"El nombre del contacto es: {nombre} y su telefono es: {telefono}")

  # 3.- Funcion que recibe parametros y no regresa valor
def solicitardatos3(nom,tel):
    nombre=nom
    telefono=tel
    print(f"El nombre del contacto es:{nombre} y su telefono es: {telefono}")
  # 2.- Funcion que no recibe parametros y regresa valor
def solicitardatos2(nom,tel):
    nombre=input("nombre:")
    telefono=input("telefono:")
    return nombre,telefono
   #4.- Funcion que recibe parametros y regresa valor
def solicitardatos4(nom,tel):
    nombre=nom
    telefono=tel
    return nombre,telefono

#invocar las funciones

solicitardatos1()

nom,tel=solicitardatos2()
print(f"\n\t :::Agenda telefonica ::: \n\t\tnombre:{nom} \n\t\ttelefono:{tel} ")

nombre=input("nombre:")
telefono=input("telefono:")
solicitardatos3(nombre,telefono)

nom,tel=solicitardatos4(nombre,telefono)
print(f"\n\t :::Agenda telefonica ::: \n\t\tnombre:{nom} \n\t\ttelefono:{tel} ")

