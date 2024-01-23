'''
Descompón el ejercicio 3 de esta sesión anterior en módulos, de forma que cada clase esté en un
módulo, y mediante instrucciones import se incluyan donde se necesiten. Utiliza un IDE avanzado
que te permita gestionar cómodamente estos archivos.
'''

# Clase Persona que tiene dni, nombre, direccion y telefono
class Persona:
    def __init__(self, d, n, di, t):
        self.__dni = d
        self.__nombre = n
        self.__direccion = di
        self.__telefono = t