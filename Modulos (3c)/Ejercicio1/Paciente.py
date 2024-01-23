from Persona import Persona
from Consulta import Consulta

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
    