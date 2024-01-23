'''
Definir una clase Cliente que almacene un código de cliente y un nombre.
En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que tienen suspendidas sus cuentas corrientes.
Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.
'''
# Definición de la clase Cliente
class Cliente:
    # Lista compartida de códigos de clientes suspendidos (atributo de clase)
    suspendidos = []

    # Método de inicialización
    def __init__(self, codigo, nombre):
        # Se inicializan los atributos codigo y nombre
        self.codigo = codigo
        self.nombre = nombre

    # Método para imprimir la información del cliente y verificar si está suspendido
    def imprimir(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
        self.esta_suspendido()
    
    # Método para verificar si el cliente está suspendido
    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("_____________________________")

    # Método para suspender al cliente 
    def suspender(self):
        Cliente.suspendidos.append(self.codigo)


# Bloque principal

# Crear instancias de la clase Cliente
cliente1 = Cliente(1, "Juan")
cliente2 = Cliente(2, "Ana")
cliente3 = Cliente(3, "Diego")
cliente4 = Cliente(4, "Pedro")

# Suspender clientes 3 y 4
cliente3.suspender()
cliente4.suspender()

# Imprimir información y estado de suspensión de cada cliente
cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

# Imprimir la lista de códigos de clientes suspendidos
print(Cliente.suspendidos)
