'''
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
'''
def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese valor: "))
        lista.append(valor)
    return lista


def obtener_mayor_y_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return mayor, menor

lista=cargar()
mayor,menor=obtener_mayor_y_menor(lista)
print("Mayor: ",mayor)
print("Menor: ",menor)
