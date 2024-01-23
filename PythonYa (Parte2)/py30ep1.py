'''
Confeccionar una función que reciba una serie de edades 
y me retorne la cantidad que son mayores o iguales a 18 
(como mínimo se envía un entero a la función)
'''
# Función a la cual le pasas una edad o muchas para saber quien o no es mayor de edad
def mayores18(edad1,*edades):
    cant=0
    if edad1>=18:
        cant=cant+1
    for x in range(len(edades)):
        if edades[x]>=18:
            cant=cant+1
    return cant

# Ejemplo de quien es mayor de edad
print("La cantidad de personas mayores a 18 son:", mayores18(23,6,8,19,24))