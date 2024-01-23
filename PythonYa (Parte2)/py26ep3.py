'''
Definir una lista de enteros por asignación en el bloque principal. 
Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa.
'''
# Definición de la función producto
def calcular_producto(lista):
    # Inicializar el producto en 1
    prod = 1
    # Iterar a través de los elementos de la lista
    for elemento in lista:
        # Multiplicar el producto por el elemento actual
        prod *= elemento
    # Retornar el resultado
    return prod

# Bloque principal

# Definir la lista de números
lista = [1, 2, 3, 4, 5]

# Imprimir la lista
print("Lista:", lista)

# Calcular y mostrar el producto de todos los elementos de la lista
print("Multiplicación de todos sus elementos:", calcular_producto(lista))
