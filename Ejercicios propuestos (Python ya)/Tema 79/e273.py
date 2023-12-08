'''
Abrir un archivo de texto con el parámetro "r+", imprimir su contenido actual y agregar luego dos líneas al final.
'''
archivo=open("datos.txt","r+") 
contenido=archivo.read()
print(contenido)
archivo.write("Añadida línea 1\n")
archivo.write("Añadida línea 2\n")
archivo.close()