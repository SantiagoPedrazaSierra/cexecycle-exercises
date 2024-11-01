# Solicita numero al usuario
numero = int(input("Ingrese un numero: "))

# Bucle para generar la tabla de multiplicar del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")