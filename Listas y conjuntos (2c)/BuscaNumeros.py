'''
Crea un programa llamado BuscaNumeros.py que le pida al usuario que escriba números. El
programa los irá añadiendo uno tras otro a una lista hasta que el usuario escriba 0. Entonces, le pedirá
que diga un número y le indicará en qué posiciones de la lista aparece ese número.
'''
valor = -1
listaNumeros = []
while valor !=0:
    numero = int(input("Introduce un número (introduce 0 para salir): "))
    listaNumeros.append(numero)
    valor = numero
encontrar = int(input("Dime el número a encontrar: "))
pos = 0
final = 0
for x in range(len(listaNumeros)):
    if encontrar == listaNumeros[x]:
        final = pos
        print("Se encuentra en la posición ", final)
    pos+=1