'''
Realiza una función que reciba una cadena y cuente cuantas veces ocurre cada uno de estos patrones sin distinguir mayúsculas y minúsculas:

Los patrones son "00" "101", "ABC", "HO".

Un carácter puede formar parte de más de un patrón encontrado.

Por ejemplo:

En la cadena "000" el patrón "00" aparece dos veces (una empieza en la posición 0 y otra empieza en la posición 1).

La función se definirá como

def numeroPatrones(texto):
Y devolverá un entero con el número de patrones encontrados en la cadena.
'''
def numeroPatrones(texto):
    # Convertir la cadena a minúsculas para no distinguir entre mayúsculas y minúsculas
    texto = texto.lower()

    # Definir los patrones
    patrones = ["00", "101", "abc", "ho"]

    # Inicializar el contador de patrones
    contador = 0

    # Iterar sobre cada patrón y contar las ocurrencias
    for patron in patrones:
        indice = texto.find(patron)
        while   indice != -1:
            contador += 1
            indice = texto.find(patron,   indice + 1)

    return contador

# Ejemplo de uso
cadena = "000"
print(numeroPatrones(cadena))  # 2
