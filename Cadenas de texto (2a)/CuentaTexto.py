'''
Crea un programa llamado CuentaTexto.py que le pida al usuario un texto, y luego le diga
cuántas veces aparece la palabra Python en ese texto
'''
texto = str(input("Introduce una cadena de texto: "))
veces = 0
while texto.find('Python')>=0:
    veces=veces +1
    texto = texto[texto.find('Python')+6:]
print("La palabra \"Python\" aparece ", veces, " veces.")