'''
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
'''
# Definición de la función obtener_menor_valor
def obtener_menor_valor():
    # Solicitar al usuario que ingrese tres valores
    valor1 = int(input("Ingrese primer valor: "))
    valor2 = int(input("Ingrese segundo valor: "))
    valor3 = int(input("Ingrese tercer valor: "))    

    # Imprimir mensaje indicando que se mostrará el menor de los tres valores
    print("Menor de los tres:")

    # Determinar y mostrar el menor de los tres valores ingresados
    if valor1 < valor2 and valor1 < valor3:
        print(valor1)
    elif valor2 < valor3:
        print(valor2)
    else:
        print(valor3)

# Bloque principal

# Llamar a la función obtener_menor_valor para la primera vez
obtener_menor_valor()

# Llamar a la función obtener_menor_valor para la segunda vez
obtener_menor_valor()

