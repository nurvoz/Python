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