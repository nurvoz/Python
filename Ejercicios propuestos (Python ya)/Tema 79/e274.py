'''
Crear un archivo de texto llamado 'datos.txt' con una codificación utf-8, almacenar tres líneas de texto. Abrir luego el archivo creado con el editor VS Code.
'''
archivo=open("datos1.txt","w", encoding="utf-8") 
archivo.write("Línea 1\n") 
archivo.write("Línea 2\n") 
archivo.write("Línea 3\n")  
archivo.close()
