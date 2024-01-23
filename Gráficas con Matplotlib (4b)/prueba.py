import matplotlib.pyplot as plt

def obtener_notas_y_nombres():
    try:
        notas_alumno1 = [float(nota) for nota in input("Ingrese las notas del primer alumno separadas por espacios: ").split()]
        notas_alumno2 = [float(nota) for nota in input("Ingrese las notas del segundo alumno separadas por espacios: ").split()]

        nombre_alumno1 = input("Ingrese el nombre del primer alumno: ")
        nombre_alumno2 = input("Ingrese el nombre del segundo alumno: ")

        if len(notas_alumno1) != len(notas_alumno2):
            raise ValueError("El número de notas debe ser el mismo para ambos alumnos.")

        return notas_alumno1, notas_alumno2, nombre_alumno1, nombre_alumno2

    except ValueError as e:
        print(f"Error: {e}. Asegúrate de ingresar notas válidas y el mismo número de notas para ambos alumnos.")
        exit()

def mostrar_grafico(notas_alumno1, notas_alumno2, nombre_alumno1, nombre_alumno2):
    plt.plot(notas_alumno1, label=nombre_alumno1, marker='o', color='blue')
    plt.plot(notas_alumno2, label=nombre_alumno2, marker='s', color='green')

    plt.title('Notas de los Alumnos')
    plt.xlabel('Número de Nota')
    plt.ylabel('Nota')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    notas_alumno1, notas_alumno2, nombre_alumno1, nombre_alumno2 = obtener_notas_y_nombres()
    mostrar_grafico(notas_alumno1, notas_alumno2, nombre_alumno1, nombre_alumno2)
