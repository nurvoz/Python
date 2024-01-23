'''
Escribe una función que reciba un texto (sin espacios) y diga si es palíndromo (True) o no (False).

La función no deberá distinguir entre mayúsculas y minúsculas.

La función debe definirse con este estilo:

def esPalindromo(texto)
'''
def esPalindromo(texto):
    # Convertir el texto a minúsculas para no distinguir entre mayúsculas y minúsculas
    texto = texto.lower()
    
    # Eliminar espacios del texto
    texto_sin_espacios = "".join(texto.split())

    # Verificar si el texto es igual a su reverso
    return texto_sin_espacios == ''.join(reversed(texto_sin_espacios))

# Ejemplos de uso con comentarios explicativos
print(esPalindromo("OTTO"))    # Salida: True, ya que "OTTO" es un palíndromo
print(esPalindromo("OtTo"))    # Salida: True, ya que "OtTo" es un palíndromo (sin distinguir mayúsculas y minúsculas)
print(esPalindromo("Pedro"))   # Salida: False, ya que "Pedro" no es un palíndromo
