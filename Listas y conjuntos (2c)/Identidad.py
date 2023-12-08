'''
Crea un programa llamado Identidad.py que le pida al usuario un tamaño de tabla N y luego le
deje rellenar los datos de N filas y N columnas de enteros. Al finalizar, le deberá decir si la tabla que ha
rellenado se corresponde o no con una matriz identidad. Una matriz identidad es aquella que tiene unos
en su diagonal principal y ceros en el resto. Por ejemplo (para un tamaño 3 x 3)
'''
N = int(input("Introduce el tamaño de la tabla N: "))

tabla = []
for i in range(N):
    fila = []
    for j in range(N):
        fila.append(int(input(f"Introduce el elemento en la posición ({i + 1}, {j + 1}): ")))
    tabla.append(fila)

identidad = True
for i in range(N):
    for j in range(N):
        if i == j and tabla[i][j] != 1:
            identidad = False
        elif i != j and tabla[i][j] != 0:
            identidad = False

if identidad:
    print("Es una matriz identidad.")
else:
    print("No es una matriz identidad.")
