











import os
os.system("clear")

paises=["mexico","brasil","españa","canada"]

pais1= {
    "nombre":"mexico",
    "capital":"cdmx",
    "poblacion":120000,
    "idioma":"español",
    "status": True
}

pais2= {
    "nombre":"brasil",
    "capital":"brasilia",
    "poblacion":140000,
    "idioma":"portugues",
    "status": True
}

pais3= {
    "nombre":"canada",
    "capital":"otawua",
    "poblacion":100000,
    "idioma":["ingles","frances"],
    "idioma":{"1":"ingles","2":"frances"},
    "status": True
}

#Funciones u operacones con los dic u objetos
print(pais1)

for i in pais1:
    print(f"{i}={pais1[i]}")

#Agregar un atributo a un diccionario

pais1.altitud=3000

for i in pais1:
    print(f"{i}={pais1[i]}")

#quiar un atributo en particular
pais1.pop("status")    