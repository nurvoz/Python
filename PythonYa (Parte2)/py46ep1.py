'''
Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.
'''
class Socio:
    def __init__(self):
        # Método de inicialización (__init__): Se ejecuta al crear una nueva instancia de la clase Socio
        self.nombre = input("Ingrese el nombre del socio: ")
        self.antiguedad = int(input("Ingrese la antigüedad del socio en el club (en años): "))

class Club:
    def __init__(self):
        # Método de inicialización (__init__): Se ejecuta al crear una nueva instancia de la clase Club
        # Se crean tres instancias de la clase Socio como atributos del Club
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def imprimir_socio_mas_antiguo(self):
        # Método para imprimir el nombre del socio con mayor antigüedad en el club
        socios = [self.socio1, self.socio2, self.socio3]
        socio_mas_antiguo = max(socios, key=lambda x: x.antiguedad)
        print(f"El socio con mayor antigüedad en el club es: {socio_mas_antiguo.nombre}")

# Crear una instancia de la clase Club
mi_club = Club()

# Imprimir el nombre del socio con mayor antigüedad en el club
mi_club.imprimir_socio_mas_antiguo()
