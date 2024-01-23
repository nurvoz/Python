'''
Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)
'''
class Punto:
    # Definición de la clase Punto
    def __init__(self, x, y):
        # Se ejecuta al crear una nueva instancia de la clase Punto
        # Se establecen las coordenadas x e y del punto con los valores proporcionados
        self.x = x
        self.y = y

    def imprimir(self):
        # Método para imprimir las coordenadas del punto
        print("Coordenada del punto")
        print("(", self.x, ",", self.y, ")")

    def imprimir_cuadrante(self):
        # Método para imprimir el cuadrante en el que se encuentra el punto
        if self.x > 0 and self.y > 0:
            print("Primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print("Segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print("Cuarto cuadrante")
            

# Crear una instancia de la clase Punto llamada punto1
punto1 = Punto(10, -2)

# Imprimir las coordenadas del punto1
punto1.imprimir()

# Imprimir el cuadrante en el que se encuentra el punto1
punto1.imprimir_cuadrante()
