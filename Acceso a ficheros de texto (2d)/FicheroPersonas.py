'''
Crea un programa llamado FicheroPersonas.py que lea información de personas (nombre y edad) de
un fichero de texto, y muestre por pantalla los datos de la persona más joven y más vieja del fichero. El
formato del fichero será como el siguiente, y se deberá almacenar en una lista antes de procesar la
información.
'''
lectura = open("datos.txt", "r")
lineas = lectura.readlines()
edad = []
max = 0
for linea in lineas:
    valores = linea.split(";")
    edad.append(valores[1])
    for e in edad:
        if int(e)>int(max):
            max = e
print(max)
