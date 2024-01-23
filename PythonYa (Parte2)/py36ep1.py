'''
Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"
'''
# Carga de datos de empleados.
def cargar_empleados():
    empleados = {}
    cant_empleados = int(input("Ingrese la cantidad de empleados: "))
    for _ in range(cant_empleados):
        legajo = input("Ingrese el número de legajo del empleado: ")
        nombre = input("Ingrese el nombre del empleado: ")
        profesion = input("Ingrese la profesión del empleado: ")
        sueldo = float(input("Ingrese el sueldo del empleado: "))
        empleados[legajo] = [nombre, profesion, sueldo]
    return empleados

# Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
def modificar_sueldo(empleados):
    legajo_modificar = input("Ingrese el número de legajo del empleado cuyo sueldo desea modificar: ")
    if legajo_modificar in empleados:
        nuevo_sueldo = float(input("Ingrese el nuevo sueldo: "))
        empleados[legajo_modificar][2] = nuevo_sueldo
        print("Sueldo modificado correctamente.")
    else:
        print("No se encontró un empleado con ese número de legajo.")

# Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"
def mostrar_analistas(empleados):
    print("Empleados con profesión 'analista de sistemas':")
    for legajo, datos in empleados.items():
        if datos[1] == "analista de sistemas":
            print(f"Legajo: {legajo}, Nombre: {datos[0]}, Sueldo: {datos[2]}")

#Cargar empleados
empleados = cargar_empleados()

# Ejemplo de modificación de sueldo
modificar_sueldo(empleados)

# Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"
mostrar_analistas(empleados)
