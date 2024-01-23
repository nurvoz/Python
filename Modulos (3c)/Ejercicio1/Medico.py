from Persona import Persona

# Clase Medico que hereda los atributos de Persona y añade la especialidad
class Medico (Persona):
    def __init__(self, d, n, di, t, e):
        super().__init__(d, n, di, t)
        self.__especialidad = e