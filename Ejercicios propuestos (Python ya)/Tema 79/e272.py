'''
Abrir el archivo de texto 'datos.txt' y luego agregar 2 líneas. Imprimir luego el archivo completo.
'''
archivo=open("datos5.txt","a")
archivo.write("nueva línea 1\n")
archivo.write("nueva línea 2\n")
archivo.close()
archivo=open("datos.txt","r")
contenido=archivo.read()
print(contenido)
archivo.close()
