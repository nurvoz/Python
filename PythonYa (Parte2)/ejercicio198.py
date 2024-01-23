'''
Plantear un programa que permita jugar a los dados. Las reglas de juego son:
se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió".

Lo primero que hacemos es identificar las clases:

Podemos identificar la clase Dado y la clase JuegoDeDados.

Luego los atributos y los métodos de cada clase:

Dado		
    atributos
        valor
    métodos
        tirar
        imprimir
        retornar_valor

JuegoDeDados
    atributos
        3 Dado (3 objetos de la clase Dado)
    métodos
        __init__
        jugar
'''
import random

# Definición de la clase Dado
class Dado:

    # Método para tirar el dado y asignar un valor aleatorio entre 1 y 6
    def tirar(self):
        self.valor = random.randint(1, 6)

    # Método para imprimir el valor actual del dado
    def imprimir(self):
        print("Valor del dado:", self.valor)

    # Método para retornar el valor actual del dado
    def retornar_valor(self):
        return self.valor

# Definición de la clase JuegoDeDados
class JuegoDeDados:

    # Método de inicialización (__init__): Se ejecuta al crear una nueva instancia de la clase JuegoDeDados
    def __init__(self):
        # Se crean tres instancias de la clase Dado
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()

    # Método para simular un juego de dados
    def jugar(self):
        # Se tira cada dado, se imprime su valor y se repite el proceso para los tres dados
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()

        # Se verifica si los valores de los tres dados son iguales
        if self.dado1.retornar_valor() == self.dado2.retornar_valor() and self.dado1.retornar_valor() == self.dado3.retornar_valor():
            print("Gano")
        else:
            print("Perdio")


# Crear una instancia de la clase JuegoDeDados llamada juego_dados
juego_dados = JuegoDeDados()

# Llamar al método jugar para simular un juego de dados
juego_dados.jugar()
