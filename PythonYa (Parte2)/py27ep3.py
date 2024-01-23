'''
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
'''
# Función para cargar una lista de 10 elementos enteros
def cargar_lista():
    lista = []
    for i in range(10):
        elemento = int(input(f"Ingrese el elemento {i + 1}: "))
        lista.append(elemento)
    return lista

# Función para generar dos listas a partir de la primera
def generar_listas(lista):
    negativos=[]
    positivos=[]
    for x in range(len(lista)):
        if lista[x]<0:
            negativos.append(lista[x])
        else:
            if lista[x]>0:
                positivos.append(lista[x])
    return [negativos,positivos]                
           
# Función para imprimir las dos listas generadas
def imprimir_listas(lista):
    for x in range(len(lista)):
        print(lista[x])


# programa principal

# Generar la lista
lista=cargar_lista()

# Generar la listas de negativos y de positivos
negativos,positivos=generar_listas(lista)

# Impresión
print("Lista con los valores negativos")
imprimir_listas(negativos)
print("Lista con los valores positivos")
imprimir_listas(positivos)