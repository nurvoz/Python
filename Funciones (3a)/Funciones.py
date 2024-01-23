'''
Crea un programa llamado Funciones.py con las siguientes funciones:
1. Una función llamada mcd que reciba dos enteros a y b como parámetros y devuelva el máximo
común divisor de esos parámetros. El máximo común divisor es el número más alto por el que se
pueden dividir los dos números.
2. Una función llamada esPrimo que reciba un número como parámetro y devuelva un booleano
indicando si el número es primo o no
Desde el programa principal, llama a la función mcd para calcular el máximo común divisor de 20 y 12
(debería dar 4), y usa la función esPrimo para sacar los números primos que haya del 1 al 50.
'''

def mcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print("El mcd es: ", mcd(20, 12))



def esPrimo(numero):
    cont = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            cont = cont + 1
    if cont == 2:
        return True
    else:
        return False

for num in range(1, 51):
        if esPrimo(num):
            print(num, end="")
            print(" ", end="")
