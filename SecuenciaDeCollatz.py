# Función para calcular la secuencia de Collatz
def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2  # Si es par
        else:
            n = 3 * n + 1  # Si es impar
    sequence.append(1)  # Añadir el 1 al final de la secuencia
    return sequence

# Función para calcular y graficar las longitudes de las secuencias de Collatz
def collatz_graph(n):
    for i in range(1, n + 1):
        sequence = collatz_sequence(i)
        length = len(sequence)
        print(f"{i} {'*' * length}")

# Solicita al usuario que ingrese un número
n = int(input("n: "))

# Genera y muestra la secuencia de Collatz para el número ingresado
print("Secuencia de Collatz:")
print(" ".join(map(str, collatz_sequence(n))))

# Genera y grafica las longitudes de las secuencias de Collatz para números menores que n
print("\nLongitudes de las secuencias de Collatz:")
collatz_graph(n)

