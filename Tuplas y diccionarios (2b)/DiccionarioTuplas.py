'''
Crea un programa llamado DiccionarioTuplas.py donde le pidas al usuario que rellene direcciones de 4
usuarios, identificados por su clave que será el DNI. Así, para cada usuario rellenará dicho DNI, y luego
los datos de la dirección como en el ejercicio anterior (nombre de calle, número de puerta y número de
piso). Almacenará los datos en un diccionario (asociando cada DNI con su dirección) y luego le pedirá al
usuario que escriba un DNI y mostrará los datos de su dirección, o el mensaje "El DNI no se encuentra
almacenado" si no existe dicha clave
'''
usuarios = {}
for i in range(4):
    dni = str(input("Introduce el dni del usuario: "))
    nombreC = str(input("Introduce el nombre de la calle: "))
    numeroPu = str(input("Introduce el número de la puerta: "))
    numeroPi = str(input("Introduce el número del piso: "))
    usuarios[dni] = (nombreC, numeroPu, numeroPi)
prueba = str(input("Escribe un dni: "))
if prueba in usuarios:
    usuario = usuarios[prueba]
    print("Nombre de la calle: ", usuario[0], "Número de la puerta: ", usuario[1],"Número del piso: ", usuario[2])
else:
    print("No existe usuario con ese dni.")