'''
Crea un programa llamado SumaSecuencia.py que le pida al usuario una secuencia de números
separados por espacios y calcule la suma total de esos números.
'''
secuencia = input("Escribe una secuencia de números separados por un espacio: ")
numeros = secuencia.split(" ")
total = 0
for i in numeros:
    total = total + int(i)
print("La suma total es: ", total)