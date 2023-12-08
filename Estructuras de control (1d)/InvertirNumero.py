'''
Crea un programa llamado InvertirNumero.py que le pida al usuario un número entero y construya
otro en otra variable que sea el original dado la vuelta. Por ejemplo, si el número inicial es 2356, debe
construir el 6532
'''
numero = int(input("Introduce un número entero: "))
digito = 0
while( numero!= 0):
    digito = int(numero % 10) 
    print(digito, end="")
    numero = (numero-digito) / 10