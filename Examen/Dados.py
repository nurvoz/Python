import random as random
import mysql.connector as mysql

class Dado:

    lista_dado1 = []
    lista_dado2 = []
    lista_dado3 = []
    media1=0
    media2=0
    media3=0

    def tirardados(n):
        lista1=[]
        lista2 = []
        lista3 = []
        if n == 1:
            for i in range(100):
                lista1.append(random.randint(1,6))
            return lista1
        elif n ==2: 
            for i in range(100):
                lista2.append(random.randint(1,6))
            return lista2
        elif n==3:
            for i in range(100):
                lista3.append(random.randint(1,6))
            return lista3

    def media(n, lista):
        total = 0
        if n == 1:
            total = sum(lista)
            print(f'El valor medio del dado 1: {total/100}')
            return total/100
        elif n ==2: 
            total = sum(lista)
            print(f'El valor medio del dado 2: {total/100}')
            return total/100
        elif n==3:
            total = sum(lista)
            print(f'El valor medio del dado 3: {total/100}')
            return total/100

    def menu():
        print("*******Menú principal*********\n")
        print("1. Tirar dados 100 veces\n")
        print("2. Mostrar valor medio dado 1\n")
        print("3. Mostrar valor medio dado 2\n")
        print("4. Mostrar valor medio dado 3\n")
        print("5. Mostrar mejor dado\n")
        print("6. Salir\n")
        print("7. 20 tiradas\n")

    def veintetiradas():
        con = mysql.connect(host="localhost", user="root", passwd="", database="dados")
        cursor = con.cursor()
        veces = 20
        while veces>0:
            insert = "insert into Datos(Fecha, num_dado, media_100tiradas) values (%s, %s, %s)"
            Dado.lista_dado1 = Dado.tirardados(1)
            Dado.lista_dado2 = Dado.tirardados(2)
            Dado.lista_dado3 = Dado.tirardados(3)
            Dado.media1= Dado.media(1, Dado.lista_dado1)
            datos = ("2024-01-16", 1, Dado.media1)
            cursor.execute(insert, datos)
            Dado.media2= Dado.media(2, Dado.lista_dado2)
            datos = ("2024-01-16", 2, Dado.media2)
            cursor.execute(insert, datos)
            Dado.media3= Dado.media(3, Dado.lista_dado3)
            datos = ("2024-01-16", 3, Dado.media3)
            cursor.execute(insert, datos)
            con.commit()
            veces = veces -1

            
    
no_valores1 = True
no_valores2 = True
no_valores3 = True
mediac1 = False
mediac2 = False
mediac3 = False
while True:
    Dado.menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion==1:
        print("Opción 1")
        dado = int(input("Que dado quieres tirar: "))
        if dado ==1:
            Dado.lista_dado1 = Dado.tirardados(dado)
            no_valores1 = False
        elif dado ==2:
            Dado.lista_dado2 = Dado.tirardados(dado)
            no_valores2 = False
        elif dado ==3:
            Dado.lista_dado3 = Dado.tirardados(dado)
            no_valores3 = False
        else:
            print("Debe ser uno de los tres dados")
    elif opcion ==2:
        print("Opción 2")
        if no_valores1:
            print("Debes introducir valores al dado 1 antes de comenzar")
        else:
            Dado.media1= Dado.media(1, Dado.lista_dado1)
            mediac1 = True
    elif opcion==3:
        print("Opcion 3")
        if no_valores2:
                print("Debes introducir valores al dado 2 antes de comenzar")
        else:
            Dado.media2= Dado.media(2, Dado.lista_dado2)
            mediac2 = True
    elif opcion ==4:
        print("Opcion 4")
        if no_valores3:
            print("Debes introducir valores al dado 3 antes de comenzar")
        else:
            Dado.media3 = Dado.media(3, Dado.lista_dado3)
            mediac3 = True
    elif opcion==5:
        print("Opcion 5")
        if no_valores1 and no_valores2 and no_valores3 :
            print("Debes tirar los tres dados antes de continuar con esta opcion")
        elif mediac1 and mediac2 and mediac3:
            print("Debes calcular las medias de los tres dados antes de continuar")
        else:
            if Dado.media1>Dado.media2:
                if Dado.media1>Dado.media3:
                    print("El mayor valor es del dado 1")
            elif Dado.media2>Dado.media1:
                if Dado.media2>Dado.media3:
                    print("El mayor valor es del dado 2")
            elif Dado.media3>Dado.media1:
                if Dado.media3>Dado.media2:
                    print("El mayor valor es del dado 3")
    elif opcion==6:
        print("Gracias por usar el programa de los 3 dados")
        print("Saliendo...")
        break
    elif opcion==7:
        Dado.veintetiradas()
    else:
        print("Opción no valida, introduzca un número válido.")