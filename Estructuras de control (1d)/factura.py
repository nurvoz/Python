'''
Crea un programa llamado Factura.py que le pida al usuario precios para una factura, hasta que
escriba 0. Entonces, el programa debe mostrar el total de la factura con 2 dígitos decimales.
'''
valor = int(input("Introduce precios para la factura: "))
total = 0
while valor>0:
    total = total+valor
    valor = int(input("Introduce precios para la factura: "))
print(f"El valor es: {total:.2f}")