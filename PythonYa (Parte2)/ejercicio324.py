'''
Confeccionar una función de orden superior que reciba un String y una función con un parámetro de tipo String que retorna un Boolean.
La función debe analizar cada elemento del String llamando a la función que recibe como parámetro, si retorna un True se agrega dicho caracter al String que se retornará.

En el bloque principal definir un String con una cadena cualquiera.

Llamar a la función de orden superior y pasar expresiones lambdas para filtrar y generar otro String con las siguientes restricciones:

Un String solo con las vocales
Un String solo con los caracteres en minúsculas
Un String con todos los caracteres no alfabéticos
'''
# Función que filtra una cadena de caracteres según un criterio definido por la función fn.
def filtrar(cadena, fn):
    # Cadena resultante después de aplicar el filtro
    cad = ""
    
    # Itera sobre cada caracter en la cadena original
    for caracter in cadena:
        # Se verifica si el caracter cumple con el criterio definido por la función fn.
        # La función fn es proporcionada como argumento y se aplica a cada caracter.
        if fn(caracter):
            # Si el caracter cumple con el criterio, se agrega a la cadena resultante.
            cad = cad + caracter
            
    # Devuelve la cadena resultante después de aplicar el filtro.
    return cad

# Ejemplo de uso
cadena = "¿Esto es la prueba 1 o la prueba 2?"

# Imprimir el string original
print("String original:")
print(cadena)

# Filtrar el string solo con las vocales
print("String solo con las vocales:")
# Se utiliza la función filtrar con una función lambda que verifica si el caracter es una vocal.
cadena_vocales = filtrar(cadena, lambda car: car in 'aeiouAEIOU')
print(cadena_vocales)

# Filtrar el string solo con los caracteres en minúscula
print("String solo con los caracteres en minúscula:")
# Se utiliza la función filtrar con una función lambda que verifica si el caracter es minúscula.
cadena_minusculas = filtrar(cadena, lambda car: car.islower())
print(cadena_minusculas)

# Filtrar el string solo con los caracteres no alfabéticos
print("String solo con los caracteres no alfabéticos:")
# Se utiliza la función filtrar con una función lambda que verifica si el caracter no es alfabético.
cadena_no_alfabeticos = filtrar(cadena, lambda car: not car.isalpha())
print(cadena_no_alfabeticos)
