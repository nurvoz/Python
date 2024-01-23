'''
Confeccionar una función que reciba entre 2 y 5 enteros. 
La misma nos debe retornar la suma de dichos valores. 
Debe tener tres parámetros por defecto.
'''
# Función sumar que devuelve la suma total de los valores que has introducido
def sumar_todos(v1,v2,v3=0,v4=0,v5=0):
    s=v1+v2+v3+v4+v5
    return s


# bloque principal

# Suma con tres valores por defecto
print("La suma de 5 + 6")
print(sumar_todos(5,6))

# Suma con dos valores por defecto
print("La suma de 1 + 2 + 3")
print(sumar_todos(1,2,3))

# Suma sin valores por defecto, todos pasados mediante variables
print("La suma de 1 + 2 + 3 + 4 + 5")
print(sumar_todos(1,2,3,4,5))