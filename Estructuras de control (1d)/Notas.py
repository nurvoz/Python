'''
Crea un programa llamado Notas.py que le pida al usuario 3 notas, y calcule la nota final según estas
reglas:
Si ninguna nota es mayor que 4, la nota final es 0
Si algunas notas son mayores que 4 (pero no todas), la nota final es 2
Si todas las notas son mayores que 4, la nota final será el 30% de la primera más el 20% de la
segunda más el 50% de la tercera
'''
nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

if(nota1 < 4 and nota2<4 and nota3<4):
    print("La media es 0")
elif(nota1 < 4 or nota2<4 or nota3<4):
        print("La media es de 2")
else:
      print("La media es "+(nota1*0.3)+(nota2*0.2)+(nota3*0.5))
