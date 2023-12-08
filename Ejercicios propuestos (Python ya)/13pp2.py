'''
Ingresar una oración que pueden tener letras tanto en mayúsculas 
como minúsculas. Contar la cantidad de vocales. 
Crear un segundo string con toda la oración en minúsculas 
para que sea más fácil disponer la condición que verifica 
que es una vocal.
'''
oracion=input("Ingrese una oracion:")
min=oracion.lower()
cant=0
x=0
while x<len(min):
    if min[x]=="a" or min[x]=="e" or min[x]=="i" or min[x]=="o" or min[x]=="u":
        cant=cant+1
    x=x+1
print("Cantidad de vocales en la oracion: ", cant)