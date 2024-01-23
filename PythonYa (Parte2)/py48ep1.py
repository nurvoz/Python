'''
Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el fin de juego (iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero.
'''
class Jugador:
    # Variable de clase que indica cuántos minutos faltan para el fin de juego
    tiempo_restante = 30

    def __init__(self, nombre, puntaje):
        # Método de inicialización (__init__): Se ejecuta al crear una nueva instancia de la clase Jugador
        self.nombre = nombre
        self.puntaje = puntaje

    def imprimir(self):
        # Método para imprimir la información del jugador
        print(f"Nombre: {self.nombre}, Puntaje: {self.puntaje}, Tiempo Restante: {Jugador.tiempo_restante} minutos")

    def pasar_tiempo(self):
        # Método para reducir en uno la variable de clase tiempo_restante
        Jugador.tiempo_restante -= 1


# Bloque principal del programa

# Crear dos instancias de la clase Jugador
jugador1 = Jugador("Carlos", 100)
jugador2 = Jugador("María", 85)

# Mostrar información inicial de los jugadores
print("Información Inicial:")
jugador1.imprimir()
jugador2.imprimir()

# Reducir la variable de clase tiempo_restante hasta llegar a cero
while Jugador.tiempo_restante > 0:
    # Llamar al método pasar_tiempo para cada jugador en cada iteración
    jugador1.pasar_tiempo()
    jugador2.pasar_tiempo()

# Mostrar información final de los jugadores
print("\nInformación Final:")
jugador1.imprimir()
jugador2.imprimir()
