'''
Definir una lista por asignación con 5 enteros. 
Mostrar por pantalla solo los elementos 
con valor iguales o superiores a 7.
'''
lista=[4, 8, 2, 10, 6]
x=0
print("Elementos: ")
for elemento in lista:
    if elemento >= 7:
        print(elemento)