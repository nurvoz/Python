'''
La sucesión de Fibonacci se define en principio como f(n)=f(n-1)+f(N-2).

Hay dos casos especiales, los casos de f(0)=0 y f(1)=1.

Más información sobre la sucesión de Fibonacci en https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
Escribe una función que reciba un entero entre 0 y 20 y calcule su número de Fibonacci. No es válido el pre calcular los valores.

La función debe definirse con este estilo:

def fibonacci(num)
'''
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # Caso general usando la fórmula f(n) = f(n-1) + f(n-2)
        a = 0
        b = 1
        for _ in range(2, num + 1):
            temp = a
            a = b
            b = temp + b
        return b

# Ejemplos de uso con comentarios explicativos
print(fibonacci(0))  # Salida: 0, ya que el término 0 de Fibonacci es 0
print(fibonacci(1))  # Salida: 1, ya que el término 1 de Fibonacci es 1
print(fibonacci(2))  # Salida: 1, ya que el término 2 de Fibonacci es 1 (0 + 1)
print(fibonacci(3))  # Salida: 2, ya que el término 3 de Fibonacci es 2 (1 + 1)
print(fibonacci(4))  # Salida: 3, ya que el término 4 de Fibonacci es 3 (1 + 2)