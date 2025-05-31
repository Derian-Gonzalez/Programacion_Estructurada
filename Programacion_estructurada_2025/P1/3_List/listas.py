#crear una lista de numeros e imprimir el contenido 
import os
os.system("cls")
numeros={100,34}
print(numeros)
#segunda forma
variable="["
for i in numeros:
    variable=f"{i},"
print(f"{variable}]")

variable="["
for i in range(0,len(numeros)):
    variable+=f"{numeros[i]},"
print(f"{variable}]")

#Ejemplo 2 crea una lista de palabras y posteriormente buscar la coincidencia de una palabra 
os.system("cls")
palabra=["utd","2025","logo","ti","2c clasica"]
palabra_buscar=input("Dame la palabra abuscar en la lista:")
if palabra_buscar in palabra:
    print("Si encontro la palabra en la lista")
else:
    print("No encontro la palabra en la lista:")    
#segunda forma
for i in palabra:
    if i==palabra_buscar:
        print("Si encontro la palabra en la lista")
    else:
        print("NNo se enconro la palbra en la lista")
#cambios 
encontro=False
cuantas=0
posiciones=[]
for i in palabra:
    if i==palabra_buscar:
        encontro=True
        cuantas+=1
        posiciones.append(palabra.index(i))
if encontro:
    print("Si encontro la palabra en la lista")
else:
     print("NNo se enconro la palbra en la lista")

#ejercicio numero cuatro
agenda=[
    {"carlos","6183728291"},
    {"carlos vi","518352842"},
    {"carlos vii","618239323"},
]
print(agenda)

for i in agenda:
    print(i)

#Segunda forma
for r in range(0,3):
    for c in range(0,2):
        print("agenda{r}{c}")

#otra manera
lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}"
        lista+"\n"
print(lista)