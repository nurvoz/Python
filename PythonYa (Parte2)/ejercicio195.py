'''
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa.
'''
# Definición de la clase Alumnos
class Alumnos:

    # Método de inicialización (__init__): Se ejecuta al crear una nueva instancia de la clase Alumnos
    def __init__(self):
        # Se inicializan las listas para almacenar nombres y notas de alumnos
        self.nombres = []
        self.notas = []

    # Método que presenta un menú de opciones y ejecuta la funcionalidad correspondiente
    def menu(self):
        opcion = 0
        # El bucle se ejecuta hasta que se seleccione la opción 4 para finalizar el programa
        while opcion != 4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion = int(input("Ingrese su opcion:"))
            # Se ejecuta la funcionalidad correspondiente según la opción seleccionada
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.notas_altas()

    # Método para cargar nombres y notas de alumnos
    def cargar(self):
        for x in range(5):
            nom = input("Ingrese nombre del alumno:")
            self.nombres.append(nom)
            no = int(input("Nota del alumno:"))
            self.notas.append(no)

    # Método para listar nombres y notas de todos los alumnos
    def listar(self):
        print("Listado completo de alumnos")
        for x in range(5):
            print(self.nombres[x], self.notas[x])
        print("_____________________")

    # Método para mostrar los nombres y notas de alumnos con notas mayores o iguales a 7
    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        for x in range(5):
            if self.notas[x] >= 7:
                print(self.nombres[x], self.notas[x])
        print("_____________________")

# Crear una instancia de la clase Alumnos llamada alumnos
alumnos = Alumnos()

# Llamar al método menu para iniciar la interacción con el usuario
alumnos.menu()
