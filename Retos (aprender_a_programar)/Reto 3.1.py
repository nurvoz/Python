cantidad = int(input("Ingrese la cantidad de dinero, debe ser múltiplo de 5: "))

if cantidad % 5 != 0:
    print("La cantidad ingresada no es un múltiplo de 5.")
else:
    billetes_500 = cantidad // 500
    billetes_200 = (cantidad % 500) // 200
    billetes_100 = ((cantidad % 500) % 200) // 100
    billetes_50 = (((cantidad % 500) % 200) % 100) // 50
    billetes_20 = ((((cantidad % 500) % 200) % 100) % 50) // 20
    billetes_10 = (((((cantidad % 500) % 200) % 100) % 50) % 20) // 10
    billetes_5 = ((((((cantidad % 500) % 200) % 100) % 50) % 20) % 10) // 5

    total_billetes = billetes_500 + billetes_200 + billetes_100 + billetes_50 + billetes_20 + billetes_10 + billetes_5

    print("El número mínimo de billetes es: ", total_billetes)
