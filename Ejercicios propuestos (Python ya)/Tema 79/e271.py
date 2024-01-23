'''
Leer el contenido del archivo de texto 'datos.txt' y almacenar sus líneas en una lista. Imprimir la cantidad de líneas que tiene el archivo y su contenido.
'''
archivo=open("datos1.txt","r")
lineas=archivo.readlines()
print("Tiene", len(lineas), "líneas")
print("El contenido del archivo")
for linea in lineas:
    print(linea, end='')
archivo.close()