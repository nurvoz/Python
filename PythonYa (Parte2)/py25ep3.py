'''
Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
'''
# Definición de la función retornar_superficie
def retornar_superficie(lado1, lado2):
    # Calcular la superficie del rectángulo
    superficie = lado1 * lado2
    # Retornar el resultado
    return superficie

# Bloque principal

# Solicitar al usuario los lados del primer rectángulo
print("Primer rectángulo")
lado1 = int(input("Ingrese lado menor del rectángulo: "))
lado2 = int(input("Ingrese lado mayor del rectángulo: "))

# Solicitar al usuario los lados del segundo rectángulo
print("Segundo rectángulo")
lado3 = int(input("Ingrese lado menor del rectángulo: "))
lado4 = int(input("Ingrese lado mayor del rectángulo: "))

# Comparar las superficies de ambos rectángulos
if retornar_superficie(lado1, lado2) == retornar_superficie(lado3, lado4):
    print("Los dos rectángulos tienen la misma superficie")
else:
    if retornar_superficie(lado1, lado2) > retornar_superficie(lado3, lado4):
        print("El primer rectángulo tiene una superficie mayor")
    else:
        print("El segundo rectángulo tiene una superficie mayor")
