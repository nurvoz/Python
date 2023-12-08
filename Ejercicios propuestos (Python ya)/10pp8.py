'''
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
'''
mañana=0
tarde=0
noche=0

for i in range(5):
    edad=int(input("Ingrese edad:"))
    mañana=mañana+edad
promañana=mañana/5
print("Promedio de edades del turno mañana:")
print(promañana)

for j in range(6):
    edad=int(input("Ingrese edad:"))
    tarde=tarde+edad
promtarde=tarde/6
print("Promedio de edades del turno tarde:")
print(promtarde)

for k in range(11):
    edad=int(input("Ingrese edad:"))
    noche=noche+edad
promnoche=noche/11
print("Promedio de edades del turno noche:")
print(promnoche)
if promañana<promtarde and promañana<promnoche:
    print("El turno mañana tiene un promedio menor de edades.")
else:
    if promtarde<promnoche:
        print("El turno tarde tiene un promedio menor de edades.")
    else:
        print("El turno noche tiene un promedio menor de edades.")