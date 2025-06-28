peliculas=[]

def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    print("\n\t\t... Oprima cualquier tecla para continuar...")
    input() 

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Peliculas ::. \n")
    peliculas.append(input("Ingresa el nombre: ").upper().strip())
    print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar las Peliculas ::. \n")
    if len(peliculas)>0:
      for i in range(0,len(peliculas)):
        print(f"\t{i+1}: {peliculas[i]}")
    else:
       print("\n\t .:: No hay peliculas en el sistema en este momento ::.")

def vaciarPeliculas():
   borrarPantalla()
   print("\n\t.:: Vaciar quitar Todas las Peliculas ::. \n")
   resp=input("¿Deseas quietar TODAS las Peliculas del sitema? (Si/No)").lower().strip()
   
   if resp=="si":
      peliculas.clear()
      print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def buscarPeliculas():


    borrarPantalla()
    print("\n\t.:: Buscar Películas ::.")
    if len(peliculas) == 0:
        print("\n\t .:: No hay películas en el sistema en este momento ::.")
        return
    
    busqueda = input("Ingresa el nombre (o parte del nombre) de la película a buscar: ").upper().strip()
    encontradas = [p for p in peliculas if busqueda in p]
    
    if len(encontradas) > 0:
        print(f"\n\tPelículas encontradas con '{busqueda}':")
        for i, pelicula in enumerate(encontradas, 1):
            print(f"\t{i}: {pelicula}")
    else:
        print(f"\n\t .:: No se encontraron películas que contengan '{busqueda}' ::.")

def buscarPeliculas():
    borrarPantalla()
    print ("\n\t.:: Buscar Peliculas ::. \n")
    pelicula_buscar=input("Ingresa el nombre de la película a buscar ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("\n\t\t No se encontro la película")
    else:
        for i in range (0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"\nLa pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i+1}")
                encontro+=1
        print(f"\nTenemos {encontro} películas con este título")
        print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def eliminarPeliculas():
    borrarPantalla()
    print ("\n\t.:: Borrar Películas ::. \n")
    pelicula_buscar=input("Ingresa el nombre de la película a eliminar ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("\n\t\t No se encontro la película")
    else:
        resp="si"
        while pelicula_buscar in peliculas and resp=="si":
            resp=input("Deseas borrar la película del sistema? (Si-No()")
            if resp=="si":
                posicion=peliculas.index(pelicula_buscar)
                print(f"\nLa pelicula que se borro {pelicula_buscar} estaba en la casilla {posicion+1}")
                peliculas.remove(pelicula_buscar)
                encontro+=1
                print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
        print(f"\n\tSe borro {encontro} películas con este título")