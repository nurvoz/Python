'''
Escribe una nueva versión del ejercicio anterior en un programa llamado Equipos.py donde,
además de la clase Jugador haya una segunda clase llamada Equipo , cuyo único atributo será el
nombre del equipo (texto), junto con un constructor para darle valor . Haz que cada jugador pueda
pertenecer a un equipo añadiendo un atributo Equipo a la clase Jugador. En el programa principal, crea
un jugador y un equipo, y asigna el equipo al jugador. Muestra por pantalla la información del jugador,
incluyendo el equipo. 
'''
class Jugador:
    def __init__(self, d, n, ne):
        self.__dorsal = d
        self.__nombre  = n
        self.__equipo = ne


    def mostrar(self):
        print(f"{self.__dorsal}, {self.__nombre}, {self.__equipo}")

class Equipo:
    def __init__(self, ne):
        self.__equipo = ne
    
    @property
    def equipo(self):
        return self.__equipo


    @equipo.setter
    def equipo(self, e):
        self.__equipo = e

e1 = Equipo("España")
j1 = Jugador(19, "Nuria", e1.equipo)
j1.mostrar()

