'''
Leer el contenido del archivo de texto 'datos.txt' línea a línea. (Con for)
'''
archivo=open("datos1.txt","r")
for linea in archivo:
    print(linea, end='')
archivo.close()
