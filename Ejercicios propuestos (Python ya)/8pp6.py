'''
De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.
'''
sueldo = int(input("Introduce el sueldo: "))
antiguedad = int(input("Introduce los años de antigüedad: "))
if sueldo < 500:
    if antiguedad >= 10:
        sueldo_a_pagar = sueldo * 1.20
        print("Sueldo a pagar:", sueldo_a_pagar)
    else:
        sueldo_a_pagar = sueldo * 1.05
        print("Sueldo a pagar:", sueldo_a_pagar)
else:
    print("Sueldo a pagar:", sueldo)