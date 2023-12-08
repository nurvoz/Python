'''
Ingresar por teclado los nombres de 5 personas 
y almacenarlos en una lista. 
Mostrar el nombre de persona menor en orden alfabético.
'''
nombres=[]
for x in range(5):
    nom=input("Ingrese nombre de persona:")
    nombres.append(nom)

menor=min(nombres)

print("La lista completa de nombres ingresado son")
print(nombres)
print("El nombre menor en orden alfabetico es:")
print(menor)