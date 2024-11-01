# Inicializa las variables para el cálculo
potencia = 1
fraccion = 0.5  # 2^(-1)
suma_total = 0

# Encabezado de las columnas
print("Potencia  Fraccion       Suma")

# Bucle para calcular cada fila de la tabla
while fraccion > 0.000001:
    suma_total += fraccion  # Suma acumulativa de las fracciones
    print(f"{potencia:<9} {fraccion:<13} {suma_total:<}")
    
    # Actualiza los valores para la siguiente iteración
    potencia += 1
    fraccion = 0.5 ** potencia  # Calcula la siguiente fracción (2^-potencia)
