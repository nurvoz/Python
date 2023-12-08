'''
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
	if valor%2==0:
'''
n = int(input("Introduce la cantidad: "))
aux = 1
pares = 0
impares = 0
while aux<=n:
    valor = int(input("Ingrese el valor: "))
    if valor%2==0:
        pares = pares +1
    else:
        impares = impares +1
    aux = aux+1
print(pares)
print(impares)