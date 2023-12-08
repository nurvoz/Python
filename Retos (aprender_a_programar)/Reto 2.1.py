
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))

precio_hora = float(input("Ingrese el precio por hora: "))

tarifa_normal = precio_hora
horas_normales = 0
horas_extra = 0

for i in range(int(horas_trabajadas)):
    if i < 35:
        horas_normales += 1
    else:
        horas_extra += 1

salario_bruto = (horas_normales * tarifa_normal) + (horas_extra * 1.5 * tarifa_normal)

impuestos_libres = 500
impuestos_25 = 0
impuestos_45 = 0
cont = 0

for i in range(int(salario_bruto)):
    if i > impuestos_libres and i<900:
        impuestos_25 += 0.25
        cont+1
    if i>900:
        impuestos_45 += 0.45

impuestos_totales = impuestos_25 + impuestos_45

salario_neto = salario_bruto - impuestos_totales

print("Salario Neto: ", salario_neto)
