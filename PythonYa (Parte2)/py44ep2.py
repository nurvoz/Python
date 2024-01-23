'''
Implementar la clase Operaciones. 
Se deben cargar dos valores enteros por teclado en el método __init__, calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.
'''
class Operaciones:
    def __init__(self):
        # Método de inicialización (__init__): Se ejecuta al crear una nueva instancia de la clase
        self.valor1 = 0
        self.valor2 = 0

    def ingresar_valores(self):
        # Solicitar al usuario que ingrese dos valores enteros
        self.valor1 = int(input("Ingrese el primer valor entero: "))
        self.valor2 = int(input("Ingrese el segundo valor entero: "))

    def suma(self):
        # Método para calcular la suma de los dos valores
        resultado = self.valor1 + self.valor2
        return resultado

    def resta(self):
        # Método para calcular la resta de los dos valores
        resultado = self.valor1 - self.valor2
        return resultado

    def multiplicacion(self):
        # Método para calcular la multiplicación de los dos valores
        resultado = self.valor1 * self.valor2
        return resultado

    def division(self):
        # Método para calcular la división de los dos valores
        if self.valor2 != 0:
            resultado = self.valor1 / self.valor2
            return resultado
        else:
            return "No es posible dividir por cero."

    def imprimir_resultados(self):
        # Método para imprimir los resultados de todas las operaciones
        print("Suma:", self.suma())
        print("Resta:", self.resta())
        print("Multiplicación:", self.multiplicacion())
        print("División:", self.division())

# Crear una instancia de la clase Operaciones
operaciones = Operaciones()

# Ingresar valores enteros
operaciones.ingresar_valores()

# Imprimir resultados de las operaciones
operaciones.imprimir_resultados()
