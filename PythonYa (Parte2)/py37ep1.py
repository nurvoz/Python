'''
Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
3) Imprimir una lista.
'''
# Carga de una lista de 10 enteros.
def cargar_lista():
    lista = []
    for _ in range(10):
        elemento = int(input("Ingrese un entero: "))
        lista.append(elemento)
    return lista

# Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
def obtener_primer_mitad(lista):
    longitud = len(lista)
    mitad = longitud // 2
    primera_mitad = lista[:mitad]
    return primera_mitad

# Imprimir una lista.
def imprimir_lista(lista):
    print("Lista:", lista)


# Paso 1: Cargar una lista de 10 enteros
mi_lista = cargar_lista()

# Paso 2: Obtener la primera mitad de la lista
primera_mitad = obtener_primer_mitad(mi_lista)

# Paso 3: Imprimir la lista resultante
imprimir_lista(primera_mitad)
