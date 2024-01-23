from Medico import Medico
from Paciente import Paciente
from Enfermero import Enfermero

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