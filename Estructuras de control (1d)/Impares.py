'''
Crea un programa llamado Impares.py que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número, separados por comas
'''
numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("Tiene que ser un número entero positivo")
else:
    impar = 1
    while impar <= numero:
        print(impar, end="")
        impar += 2
        if impar <= numero:
            print(", ", end="")
