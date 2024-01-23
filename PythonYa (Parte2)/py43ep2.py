'''
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, 
imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. 
El nombre de la clase llamarla Triangulo.
'''
# Definición de la clase Triangulo
class Triangulo:
    # Método de inicialización (__init__): Se ejecuta al crear una nueva instancia de la clase
    def __init__(self):
        # Inicialización de los lados a 0
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0

    # Método para inicializar los lados del triángulo
    def inicializar_lados(self):
        # Solicitar al usuario que ingrese los lados del triángulo
        self.lado1 = float(input("Ingrese el primer lado del triángulo: "))
        self.lado2 = float(input("Ingrese el segundo lado del triángulo: "))
        self.lado3 = float(input("Ingrese el tercer lado del triángulo: "))

    # Método para imprimir el lado mayor del triángulo
    def imprimir_lado_mayor(self):
        # Utiliza la función max() para obtener el lado mayor y lo imprime
        print("El lado mayor es:", max(self.lado1, self.lado2, self.lado3))

    # Método para verificar si el triángulo es equilátero
    def es_equilatero(self):
        # Retorna True si los tres lados son iguales, indicando que el triángulo es equilátero
        return self.lado1 == self.lado2 == self.lado3

# Crear una instancia de la clase Triangulo
triangulo = Triangulo()

# Inicializar los lados del triángulo
triangulo.inicializar_lados()

# Imprimir el lado mayor del triángulo
triangulo.imprimir_lado_mayor()

# Verificar si el triángulo es equilátero y mostrar el resultado
if triangulo.es_equilatero():
    print("El triángulo es equilátero.")
else:
    print("El triángulo no es equilátero.")

