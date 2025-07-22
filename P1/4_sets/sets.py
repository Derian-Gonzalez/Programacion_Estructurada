








"""import os 
os.system("cls")

#paises=["mexico","brasil","españa","canada","canada"]
#print(paises)
paises={"mexico","brasil","españa","canada","canada"}
print(paises)

varios={True,"cadena",23,3.1416}
print(varios)

paises.add("Mexico")
print(paises)

varios.pop()
print(varios)
#pop en este caso no lleva parametros, este es un subprograma que no recibe y regresa calquier cosa 

varios.remove("cadena")
print(varios)

#subprograma que recibe y no regresa 

#ejemplo crear un programa que solicite los email de los alumnos de la utd almacenar en una lisa y posteriormente
#mostrar en pantalla los email sin duplicados """

#ejemplo crear un programa que solicite los email de los alumnos de la utd almacenar en una lista y posteriormente
#mostrar en pantalla los email sin duplicados 


"""cantidad = int(input("¿Cuántos correos deseas ingresar?: "))


emails = []


for i in range(cantidad):
    email = input(f"Ingrese el correo #{i+1}: ").strip().lower()
    emails.append(email)


emails_unicos = list(set(emails))


print("\nCorreos únicos ingresados:")
for correo in emails_unicos:
    print(correo)"""


emails=[]
resp="si"

while resp=="si":
    emails.append(input("escribe un email: "))
    resp=input("Deseas agregar otro email?").lower()


emails_set=set(emails)   
emails=list(emails_set) 
print(emails)
