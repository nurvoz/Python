'''
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
Llamarla desde el bloque principal del programa 3 veces con string distintos.
'''
# Definición de la función contar_vocales
def contar_vocales(palabra):
    # Inicializar la variable cantidad que almacenará la cantidad de vocales en la palabra
    cantidad = 0
    
    # Iterar a través de cada letra en la palabra
    for letra in palabra:
        # Verificar si la letra, convertida a minúscula, está en el conjunto de vocales
        if letra.lower() in "aeiou":
            # Incrementar la cantidad de vocales encontradas
            cantidad += 1
    
    # Imprimir el resultado, indicando la cantidad de vocales en la palabra
    print("Cantidad de vocales en la palabra", palabra, "es", cantidad)

# Bloque principal

# Llamar a la función contar_vocales con la palabra "hola"
contar_vocales("hola")

# Llamar a la función contar_vocales con la palabra "administracion"
contar_vocales("administracion")

# Llamar a la función contar_vocales con la palabra "correr"
contar_vocales("correr")

