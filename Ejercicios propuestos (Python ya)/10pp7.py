'''
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
'''
negativos=0
positivos=0
quince=0
suma=0
for x in range(10):
    numero=int(input("Ingrese número:"))
    if numero<0:
        negativos+=1
    else:
        if numero>0:
            positivos+=1
    if numero%15==0:
        quince+=1
    if numero%2==0:
        suma=suma+numero

print("Valores negativos:", negativos)
print("Valores positivos:", positivos)
print("Valores múltiplos de 15:", quince)
print("Suma de los valores pares:", suma)