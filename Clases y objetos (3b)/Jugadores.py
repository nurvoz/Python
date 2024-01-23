'''
Escribe un programa en Python llamado Jugadores.py que defina una clase llamada Jugador , con
atributos dorsal (numérico) y nombre (texto). Define el constructor para darles valor y un método que
muestre la información de un jugador con el formato dorsal. Nombre. . Por ejemplo:
16. Pau Gasol . En el programa principal, crea un par de jugadores con sus datos, y muestra su
información por pantalla. 
'''
class Jugador:
    def __init__(self, d, n):
        self.__dorsal = d
        self.__nombre  = n

    def mostrar(self):
        print(f"{self.__dorsal}. {self.__nombre}")

p1 = Jugador(19, "Nuria")
p2 = Jugador(34, "Juan")
p1.mostrar()
p2.mostrar()