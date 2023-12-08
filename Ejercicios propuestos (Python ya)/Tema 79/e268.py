'''
Leer el contenido del archivo de texto 'datos.txt'.
'''
archivo=open("datos2.txt","r")
leer=archivo.read()
print(leer)
archivo.close()