'''
Leer el contenido del archivo de texto 'datos.txt' línea a línea.
'''
archivo=open("datos3.txt","r")
linea=archivo.readline()
while linea!='':
    print(linea, end='')
    linea=archivo.readline()
archivo.close()
