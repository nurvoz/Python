'''
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es ""
'''
frase=input("Ingrese una oracion:")
espacios_blancos = 0
for caracter in frase:
    if caracter == " ":
        espacios_blancos += 1
print("Cantidad de espacios en blanco: ", espacios_blancos)