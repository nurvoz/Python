'''
Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.
'''
# Define los diez primeros números, por defecto, de la tabla de multiplicar de un número
def tabla(numero, terminos=10):
    for x in range(terminos):
        va=x*numero
        print(va,",",sep="",end="") # sep para que no tenga una separación y end para evitar el salto de linea

    

# bloque principal

# Los 10 primeros terminos de la tabla del 3
print("Tabla del 3")
tabla(3)
print()

# Los 5 primeros terminos de la tabla del 3
print("Tabla del 3 con 5 terminos")
tabla(3,5)
print()

# Los 20 primeros terminos de la tabla del 3
print("Tabla del 3 con 20 terminos")
tabla(terminos=20,numero=3)
print()