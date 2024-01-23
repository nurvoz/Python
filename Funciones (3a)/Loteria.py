'''
Crea un programa llamado Loteria.py que le pida al usuario que introduzca los 6 números que
juega a la lotería (separados por espacios). Entonces, deberá crear una lista con ellos, ordenarla
ascendentemente e imprimirla en pantalla. Además, el programa debe indicar si es una lista válida (es
decir, los números deben estar entre 1 y 49, inclusive, sin repetirse). Por ejemplo:
Introduce los 6 números de la lotería separados por espacios
1 20 12 20 6 50
[1, 6, 12, 20, 20, 50]
La lista NO es válida:
Hay números repetidos
Hay números menores que 1 o mayores que 49
'''

def listaValida(numeros):
    if len(numeros) != len(set(numeros)):
        return False, "Hay números repetidos"

    for numero in numeros:
        if numero < 1 or numero > 49:
            return False, "Hay números menores que 1 o mayores que 49"

    return True

def main():
    try:
        entrada_usuario = input("Introduce los 6 números de la lotería separados por espacios: ")
        numeros = [int(num) for num in entrada_usuario.split()]
    except ValueError:
        print("Error: Ingresa números válidos.")
        return

    es_valida, mensaje_error = listaValida(numeros)

    if es_valida:
        numeros.sort()
        print(numeros)
    else:
        print(f"La lista NO es válida:\n{mensaje_error}")


