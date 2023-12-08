'''
Crea un programa llamado ListaInvertida.py que le pida al usuario que introduzca un conjunto
de nombres separados por comas, y le muestre por pantalla la misma lista en orden inverso.
'''
nombres = str(input("Introduce un conjunto de nombres separados por comas: "))
lista = nombres.split(',')
lista.reverse
print(lista)