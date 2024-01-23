'''
Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.
'''
class Cuenta:
    def __init__(self, titular, monto):
        # Método de inicialización (__init__): Se ejecuta al crear una nueva instancia de la clase Cuenta
        self.titular = titular
        self.monto = monto

    def mostrar_informacion(self):
        # Método para mostrar la información común de la cuenta
        print(f"Titular: {self.titular}, Monto: {self.monto}")

class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        # Llamada al método __init__ de la clase Cuenta
        super().__init__(titular, monto)

    def generar_intereses(self):
        # Método específico de la clase CajaAhorro (no genera intereses)
        print("La cuenta de ahorro no genera intereses.")

class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, tasa_interes):
        # Llamada al método __init__ de la clase Cuenta
        super().__init__(titular, monto)
        # Atributos específicos de la clase PlazoFijo
        self.plazo = plazo
        self.tasa_interes = tasa_interes

    def mostrar_informacion(self):
        # Sobrescribe el método de la clase base para incluir información específica de PlazoFijo
        super().mostrar_informacion()
        print(f"Plazo: {self.plazo} días, Tasa de Interés: {self.tasa_interes}%")


# Crear una instancia de la clase CajaAhorro
caja_ahorro = CajaAhorro("Juan Pérez", 5000)

# Crear una instancia de la clase PlazoFijo
plazo_fijo = PlazoFijo("Ana García", 10000, 30, 5)

# Mostrar información de ambas cuentas
print("\nInformación de Caja de Ahorro:")
caja_ahorro.mostrar_informacion()

print("\nInformación de Plazo Fijo:")
plazo_fijo.mostrar_informacion()
