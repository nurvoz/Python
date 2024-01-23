'''
Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
Definir dos objetos de la clase Alumno.
'''
class Alumno:
    # Definición de la clase Alumno
    def inicializar(self, nombre, nota):
        # Método para inicializar los atributos nombre y nota del alumno
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        # Método para imprimir el nombre y la nota del alumno
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def mostrar_estado(self):
        # Método para mostrar el estado del alumno (Regular o Libre) según su nota
        if self.nota >= 4:
            print("Regular")
        else:
            print("Libre")


# Bloque principal

# Crear una instancia de la clase Alumno llamada alumno1
alumno1 = Alumno()

# Inicializar los atributos de alumno1 con el método inicializar
alumno1.inicializar("Diego", 2)

# Imprimir información del alumno1
alumno1.imprimir()

# Mostrar el estado del alumno1
alumno1.mostrar_estado()

# Crear otra instancia de la clase Alumno llamada alumno2
alumno2 = Alumno()

# Inicializar los atributos de alumno2 con el método inicializar
alumno2.inicializar("Ana", 10)

# Imprimir información del alumno2
alumno2.imprimir()

# Mostrar el estado del alumno2
alumno2.mostrar_estado()
