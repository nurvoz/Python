'''
Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.
'''
lista_enteros =[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista_enteros .append(valor)

print("Lista original", lista_enteros )

lista_nueva =[]
pos=0
while pos<len(lista_enteros ):
    if lista_enteros [pos]>=10:
        lista_nueva .append(lista_enteros .pop(pos))
    else:
        pos=pos+1

print("Antes: ", lista_enteros )
print("Lista generada depués: ", lista_nueva )