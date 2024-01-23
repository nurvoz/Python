'''
Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando subíndices negativos.
'''
# Solicitar al usuario que ingrese una cadena de caracteres
cadena = input("Ingresar una cadena: ")

# Inicializar el índice en -1 para acceder al último carácter de la cadena
indice = -1

# Recorrer la cadena utilizando un bucle for y mostrar los caracteres en orden inverso
for x in range(len(cadena)):
    # Imprimir el carácter actual utilizando el índice negativo
    print(cadena[indice], end="")

    # Decrementar el índice para acceder al siguiente carácter hacia el final de la cadena
    indice = indice - 1
