'''
Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor su número telefónico:
1) Carga de contactos y su número telefónico.
2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.
3) Imprimir la lista completa de contactos con sus números telefónicos.
'''
# Carga de contactos y sus números telefónicos.
def cargar():
    # Se inicializa un diccionario para almacenar los contactos y sus números telefónicos.
    contactos = {}
    # Se utiliza un bucle while para permitir la carga de múltiples contactos.
    continua = "s"
    while continua == "s":
        nombre = input("Ingrese el nombre del contacto:")
        telefono = input("Ingrese el número de teléfono:")
        # Se agrega el contacto al diccionario.
        contactos[nombre] = telefono
        # Se pregunta al usuario si desea ingresar otro contacto.
        continua = input("¿Ingresar otro contacto? [s/n]: ")
    return contactos

# Permitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.
def modificar_telefono(contactos):
    nombre = input("Ingrese el nombre del contacto para modificar el teléfono:")
    # Se verifica si el nombre del contacto existe en el diccionario.
    if nombre in contactos:
        telefono = input("Ingrese el nuevo número telefónico: ")
        # Se actualiza el número telefónico del contacto.
        contactos[nombre] = telefono
    else:
        print("No existe un contacto con el nombre ingresado.")

# Imprimir la lista completa de contactos con sus números telefónicos.
def imprimir(contactos):
    print("Listado de todos los contactos:")
    # Se utiliza un bucle for para recorrer el diccionario e imprimir cada contacto con su número telefónico.
    for nombre in contactos:
        print(nombre, contactos[nombre])

# Ejemplo de uso
contactos = cargar()  # Llamada a la función cargar para ingresar contactos.
modificar_telefono(contactos)  # Llamada a la función modificar_telefono para cambiar un número telefónico.
imprimir(contactos)  # Llamada a la función imprimir para mostrar la lista completa de contactos.
