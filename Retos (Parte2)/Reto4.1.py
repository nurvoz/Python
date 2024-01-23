'''
El factorial de n se define en principio como el producto de todos los números enteros positivos desde 1 (es decir, los números naturales) hasta n. En el caso de 0, el resultado es 1.

Más información sobre factorial en https://es.wikipedia.org/wiki/Factorial
Escribe una función que reciba un entero entre 0 y 10 y calcule su factorial. No es válido el pre calcular los valores.

La función debe definirse con este estilo:

def factorial(num):
'''
def factorial(num):
    # Verifica si el número está fuera del rango permitido (0 a 10)
    if num < 0 or num > 10:
        raise ValueError("El número debe estar en el rango de 0 a 10")
    
    # Inicializa el resultado en 1, ya que el factorial de 0 es 1
    result = 1
    
    # Utiliza un bucle for para multiplicar los números desde 1 hasta num
    for i in range(1, num + 1):
        result *= i
    
    # Retorna el resultado final del factorial
    return result

# Ejemplos de uso con 
print(factorial(0))  # Salida: 1
print(factorial(1))  # Salida: 1
print(factorial(2))  # Salida: 2
print(factorial(3))  # Salida: 6
print(factorial(4))  # Salida: 24
print(factorial(5))  # Salida: 120
print(factorial(6))  # Salida: 720
print(factorial(7))  # Salida: 5040
print(factorial(8))  # Salida: 40320
print(factorial(9))  # Salida: 362880
print(factorial(10))  # Salida: 3628800
