'''
Haz un programa que le pida al usuario un nombre de imagen, la cargue y, si existe, le pida
continuamente tamaños a los que la quiera escalar (ancho y alto), y guarde una copia de la imagen
original con ese tamaño. El nombre de cada imagen escalada tendrá el patrón
ancho_alto_nombreFicheroOriginal. El proceso terminará cuando el usuario ponga la anchura o altura a
0.
'''
# Importamos la libreria PIL, antes de este deberemos de hacer ejecutado
# pip install Pillow 
from PIL import Image

# Creamo una funcion a la cual le pasaremos el nombre de la imagen / ruta que vamos a usar
def imagen(nombre_fichero):
    try:
        # Cargar la imagen original
        imagen_original = Image.open(nombre_fichero)

        while True:
            # Pedir al usuario el ancho deseado
            ancho = int(input("Ingrese el ancho de la imagen (0 para salir): "))
            if ancho == 0:
                print("Proceso terminado.")
                break

            # Pedir al usuario la altura deseada
            alto = int(input("Ingrese la altura de la imagen (0 para salir): "))
            if alto == 0:
                print("Proceso terminado.")
                break

            # Escalar la imagen
            imagen_escalada = imagen_original.resize((ancho, alto))

            # Crear el nombre del nuevo fichero
            nuevo_nombre = f"{ancho}_{alto}_{nombre_fichero}"

            # Guardar la imagen escalada
            imagen_escalada.save(nuevo_nombre)
            print(f"Imagen escalada guardada como {nuevo_nombre}")

    # Controlamos las excepciones en caso de que no se encuentre el archivo o contralos las excepciones a nivel general
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_fichero}")
    except Exception as e:
        print(f"Error: {e}")


# Hacemos la función main donde hacemos llamada a la funcion que hemos creado
# Pedir al usuario el nombre de la imagen
nombre_imagen = input("Ingrese el nombre de la imagen: ")
imagen(nombre_imagen)
