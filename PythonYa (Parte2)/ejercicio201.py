'''
Ahora plantearemos otro problema empleando herencia. Supongamos que necesitamos implementar dos clases que llamaremos Suma y Resta. Cada clase tiene como atributo valor1, valor2 y resultado. Los métodos a definir son cargar1 (que inicializa el atributo valor1), carga2 (que inicializa el atributo valor2), operar (que en el caso de la clase "Suma" suma los dos atributos y en el caso de la clase "Resta" hace la diferencia entre valor1 y valor2), y otro método mostrar_resultado.

Si analizamos ambas clases encontramos que muchos atributos y métodos son idénticos. En estos casos es bueno definir una clase padre que agrupe dichos atributos y responsabilidades comunes.

La relación de herencia que podemos disponer para este problema es:

                                        Operacion

                        Suma                              Resta
Solamente el método operar es distinto para las clases Suma y Resta (esto hace que no lo podamos disponer en la clase Operacion en principio), luego los métodos cargar1, cargar2 y mostrar_resultado son idénticos a las dos clases, esto hace que podamos disponerlos en la clase Operacion. Lo mismo los atributos valor1, valor2 y resultado se definirán en la clase padre Operacion.
'''
# Definición de la clase Operacion
class Operacion:

    # Método de inicialización 
    def __init__(self):
        # Se inicializan los atributos valor1, valor2 y resultado
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    # Método para cargar el primer valor desde la entrada del usuario
    def cargar1(self):
        self.valor1 = int(input("Ingrese primer valor:"))

    # Método para cargar el segundo valor desde la entrada del usuario
    def cargar2(self):
        self.valor2 = int(input("Ingrese segundo valor:"))

    # Método para mostrar el resultado de la operación
    def mostrar_resultado(self):
        print(self.resultado)

    # Método para realizar la operación 
    def operar(self):
        pass


# Definición de la clase Suma, que hereda de la clase Operacion
class Suma(Operacion):

    # Método para realizar la suma
    def operar(self):
        self.resultado = self.valor1 + self.valor2


# Definición de la clase Resta, que hereda de la clase Operacion
class Resta(Operacion):

    # Método para realizar la resta
    def operar(self):
        self.resultado = self.valor1 - self.valor2


# Crear una instancia de la clase Suma llamada suma1
suma1 = Suma()

# Cargar valores y realizar la suma
suma1.cargar1()
suma1.cargar2()
suma1.operar()

# Mostrar el resultado de la suma
print("La suma de los dos valores es")
suma1.mostrar_resultado()

# Crear una instancia de la clase Resta llamada resta1
resta1 = Resta()

# Cargar valores y realizar la resta
resta1.cargar1()
resta1.cargar2()
resta1.operar()

# Mostrar el resultado de la resta
print("La resta de los valores es:")
resta1.mostrar_resultado()
