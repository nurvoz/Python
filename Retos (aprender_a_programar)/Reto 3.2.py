total_numeros = int(input("Cuantos números quiere introducir: "))

numero_mas_alto = float('-inf')
numero_mas_bajo = float('inf')

for _ in range(total_numeros):
    numero = int(input())

    if numero > numero_mas_alto:
        numero_mas_alto = numero
    if numero < numero_mas_bajo:
        numero_mas_bajo = numero

print(numero_mas_alto, numero_mas_bajo)
