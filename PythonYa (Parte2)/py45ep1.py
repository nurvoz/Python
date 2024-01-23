'''
Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
'''
class AgendaPersonal:
    def __init__(self):
        # Inicialización de la agenda como un diccionario vacío
        self.agenda = {}

    # Carga de un contacto en la agenda.
    def cargar_contacto(self):
        # Método para cargar un contacto en la agenda
        nombre = input("Ingrese el nombre de la persona: ")
        telefono = input("Ingrese el número de teléfono: ")
        mail = input("Ingrese el correo electrónico: ")
        self.agenda[nombre] = {'Telefono': telefono, 'Mail': mail}
        print(f"Contacto {nombre} cargado correctamente.")

    # Listado completo de la agenda.
    def listar_agenda(self):
        # Método para mostrar el listado completo de la agenda
        print("Listado completo de la agenda:")
        for nombre, datos in self.agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {datos['Telefono']}, Correo: {datos['Mail']}")
        print()

    # Consulta ingresando el nombre de la persona.
    def consultar_contacto(self):
        # Método para consultar un contacto ingresando el nombre
        nombre_consulta = input("Ingrese el nombre de la persona a consultar: ")
        if nombre_consulta in self.agenda:
            datos = self.agenda[nombre_consulta]
            print(f"Nombre: {nombre_consulta}, Teléfono: {datos['Telefono']}, Correo: {datos['Mail']}")
        else:
            print("No se encontró el contacto en la agenda.")

    # Modificación de su teléfono y mail.
    def modificar_contacto(self):
        # Método para modificar teléfono y correo de un contacto
        nombre_modificar = input("Ingrese el nombre de la persona a modificar: ")
        if nombre_modificar in self.agenda:
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            nuevo_mail = input("Ingrese el nuevo correo electrónico: ")
            self.agenda[nombre_modificar]['Telefono'] = nuevo_telefono
            self.agenda[nombre_modificar]['Mail'] = nuevo_mail
            print(f"Contacto {nombre_modificar} modificado correctamente.")
        else:
            print("No se encontró el contacto en la agenda.")

    # Menú de la agenda
    def menu(self):
        # Método que muestra el menú y gestiona las opciones
        while True:
            print("\nMenú de la Agenda Personal:")
            print("1- Cargar un contacto en la agenda.")
            print("2- Listado completo de la agenda.")
            print("3- Consulta ingresando el nombre de la persona.")
            print("4- Modificación de su teléfono y correo.")
            print("5- Finalizar programa.")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                self.cargar_contacto()
            elif opcion == '2':
                self.listar_agenda()
            elif opcion == '3':
                self.consultar_contacto()
            elif opcion == '4':
                self.modificar_contacto()
            elif opcion == '5':
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

# Crear una instancia de la clase AgendaPersonal y ejecutar el menú
agenda_personal = AgendaPersonal()
agenda_personal.menu()
