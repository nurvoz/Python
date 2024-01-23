'''
Crea un programa llamado Tuplas.py donde le pidas al usuario que rellene su dirección postal, que
estará formada por su nombre de calle (texto), número de puerta (entero) y número de piso (entero).
Almacena los datos en una tupla y luego muestra por pantalla el resultado (campo a campo).
'''
calle = str(input("Introduce el nombre de la calle: "))
puerta = int(input("Introduce el nombre de la puerta: "))
piso = int(input("Introduce el nombre del piso: "))
tupla = (calle, puerta, piso)
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla)