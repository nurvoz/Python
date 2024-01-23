from Persona import Persona

# Clase Enfermero que hereda los tributos de Persona y añade planta
class Enfermero (Persona):
    def __init__(self, d, n, di, t, p):
        super().__init__(d, n, di, t)
        self.__planta = p