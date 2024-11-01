# Función para calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Inicializa variables
n = 10  # Comenzamos desde 10!
suma_e = 0  # Suma acumulada de e
diferencia = float('inf')  # Inicializa la diferencia en infinito

# Bucle para calcular la suma hasta que la diferencia sea menor que 0.0001
while diferencia >= 0.0001:
    nuevo_sumando = factorial(n)  # Calcula n!
    suma_e += nuevo_sumando  # Suma el nuevo sumando
    diferencia = nuevo_sumando / (factorial(n - 1))  # Calcula la diferencia entre el nuevo y el anterior
    n += 1  # Aumenta n para el siguiente factorial

# Muestra el valor aproximado de e
print(f"Valor aproximado de e: {suma_e}")
