'''
En un hospital hay diferentes tipos de personal: médicos, enfermeros y administrativos. De todos
guardamos su información básica (dni, nombre, dirección y teléfono), de los médicos almacenamos
también su especialidad, y de los enfermeros la planta en la que trabajan. 
Al hospital acuden pacientes. De todos ellos se guarda un historial con su dni, nombre, dirección,
teléfono, y un conjunto de pruebas y consultas que hayan hecho en el hospital. De cada prueba o
consulta guardamos la fecha en que se hizo, y el médico que le atendió 
Define las clases necesarias para el enunciado propuesto en un programa llamado Hospital.py. Define
un programa principal que cree un array de personal de hospital con varios médicos y enfermeros.
Define un paciente con sus datos, y dale de alta diversas pruebas realizadas por varios médicos.
Finalmente, trata de mostrar por pantalla los datos completos del paciente, incluyendo su historial de
pruebas.
'''
# Clase Persona que tiene dni, nombre, direccion y telefono
class Persona:
    def __init__(self, d, n, di, t):
        self.__dni = d
        self.__nombre = n
        self.__direccion = di
        self.__telefono = t

# Clase Medico que hereda los atributos de Persona y añade la especialidad
class Medico (Persona):
    def __init__(self, d, n, di, t, e):
        super().__init__(d, n, di, t)
        self.__especialidad = e

# Clase Enfermero que hereda los tributos de Persona y añade planta
class Enfermero (Persona):
    def __init__(self, d, n, di, t, p):
        super().__init__(d, n, di, t)
        self.__planta = p

# Clase Paciente que hereda de los atributos de Persona y añade conunto y consultas
class Paciente (Persona):
    def __init__(self, d, n, di, t, cj, c):
        super().__init__(d, n, di, t)
        self.__conjunto = cj
        self.__consulta= []
    
    # Método para agregar consultas
    def agregar_consulta(self, fecha, medico):
        consulta = Consulta(fecha, medico)
        self.__consulta.append(consulta)

    # Método para mostrar las consultas
    def mostrar_historial(self):
        for consulta in self.__consulta:
            print(f"  {consulta}. Fecha: {consulta.fecha}, Médico: {consulta.medico.nombre}, Especialidad: {consulta.medico.especialidad}")
    
# Clase Consulta que tiene por atributos la fech ay el médico 
class Consulta:
    def __init__(self, f, m):
        self.__fecha = f
        self.__medico = m

    # Getter
    @property
    def fecha(self):
        return self.__fecha
    
    # Setter
    @fecha.setter
    def fecha(self, f):
        self.__fecha=f
    
    # Getter
    @property
    def medico(self):
        return self.__medico

    # Setter
    @medico.setter
    def medico(self, m):
        self.__medico=m

# Creamos la lista donde vamos a meter al personal que trabaja en el hospital
personal = []

# Crear médicos
medico1 = Medico("12345678A", "Dr. López", "Calle A", "123456789", "Cardiología")
medico2 = Medico("87654321B", "Dr. Martínez", "Calle B", "987654321", "Neurología")

# Añadimos los medicos a la lista
personal.append(medico1)
personal.append(medico2)

# Crear enfermero
enfermero1 = Enfermero("98765432C", "Enfermero García", "Calle C", "987123456", "Planta 2")

# Añadimos el enfermero a la lista de personal
personal.append(enfermero1)

# Crear paciente
paciente1 = Paciente("11111111X", "Juan Pérez", "Calle D", "555555555", None, None)

# Agregar consulta al paciente
paciente1.agregar_consulta("2023-01-01", personal[0])
paciente1.agregar_consulta("2023-02-15", personal[1])

# Mostrar historial del paciente
print("Historial de consultas del paciente:")
paciente1.mostrar_historial()