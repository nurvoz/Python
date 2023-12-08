'''
Crea un programa llamado MayorMenor.py que le pida al usuario que introduzca una secuencia de N
números positivos (primero el usuario deberá indicar cuántos números va a introducir). Al final del
proceso, el programa deberá mostrar por pantalla el valor del número mayor y el menor introducidos
por el usuario.
'''
numeros = int(input("Introduce cuantos valores quieres introducir: "))
print("Introduce ",numeros, " números: ")
mayor = 0
menor = 0
for i in range(numeros):
    valor = int(input())
    if mayor == 0:
        mayor = valor
    if menor == 0:
        menor = valor
    if (valor > mayor):
        mayor = valor
    if(valor < menor):
        menor = valor

print("El mayor es ",mayor)
print("El menor es ",menor)