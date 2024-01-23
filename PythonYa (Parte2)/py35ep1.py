'''
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
'''
# Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
def cargar_alumnos():
    alumnos = {}
    for _ in range(3):
        dni = input("Ingrese el DNI del alumno: ")
        materias = []
        cant_materias = int(input("Ingrese la cantidad de materias cursadas por el alumno: "))
        for _ in range(cant_materias):
            materia = input("Nombre de la materia: ")
            nota = float(input("Nota de la materia: "))
            materias.append((materia, nota))
        alumnos[dni] = materias
    return alumnos

# Listado de todos los alumnos con sus notas
def listar_alumnos(alumnos):
    print("Listado de todos los alumnos con sus notas:")
    for dni, materias in alumnos.items():
        print(f"DNI: {dni}")
        for materia, nota in materias:
            print(f"  {materia}: {nota}")
        print()

# Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
def consultar_alumno(alumnos):
    dni_consulta = input("Ingrese el DNI del alumno a consultar: ")
    if dni_consulta in alumnos:
        print(f"Materias y notas del alumno con DNI {dni_consulta}:")
        for materia, nota in alumnos[dni_consulta]:
            print(f"{materia}: {nota}")
    else:
        print("No se encontró un alumno con ese DNI.")

# Ejemplo de uso
alumnos = cargar_alumnos()
listar_alumnos(alumnos)
consultar_alumno(alumnos)