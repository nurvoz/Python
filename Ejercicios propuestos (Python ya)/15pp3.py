'''
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
'''
man=[]
tar=[]

print("TURNO MAÑANA")
for x in range(4):
    valor=float(input("Ingrese sueldo:"))
    man.append(valor)

print("TURNO TARDE")
for x in range(4):
    valor=float(input("Ingrese sueldo:"))
    tar.append(valor)

print("Turno manana")
print(man)
print("Turno tarde")
print(tar)