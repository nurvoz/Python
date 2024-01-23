'''
Crea un programa llamado Contar.py que reciba como parámetros del programa principal dos datos
(numéricos) y realice un conteo desde el primero hasta el segundo. Si no se reciben los dos datos
mostraremos un mensaje de error y finalizaremos.
'''
import sys

def contar(inicio, fin):
    for num in range(inicio, fin + 1):
        print(num)

if len(sys.argv) != 3:
    print("Error: Deben proporcionarse dos argumentos numéricos.")
    sys.exit(1)

try:
    inicio = int(sys.argv[1])
    fin = int(sys.argv[2])
except ValueError:
    print("Error: Los argumentos deben ser números enteros.")
    sys.exit(1)
    
contar(inicio, fin)