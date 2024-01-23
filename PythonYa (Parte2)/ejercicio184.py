'''
Podemos definir un nombre distinto para una funcionalidad que importamos de otro módulo. Esto puede tener como objetivo que nuestro programa sea más legible o evitar que un nombre de función que importamos colisione con un nombre de función de nuestro propio módulo.

Resolveremos el mismo problema anterior pero definiendo dos alias para las funciones sqrt y pow del módulo math.
'''
# Importar funciones específicas del módulo math y darles nombres cortos
from math import sqrt as raiz, pow as elevar

# Solicitar al usuario que ingrese un valor entero
valor = int(input("Ingrese un valor entero:"))

# Calcular la raíz cuadrada del valor usando la función raiz
r1 = raiz(valor)

# Calcular el cubo del valor usando la función elevar
r2 = elevar(valor, 3)

# Imprimir los resultados
print("La raiz cuadrada es", r1)
print("El cubo es", r2)
