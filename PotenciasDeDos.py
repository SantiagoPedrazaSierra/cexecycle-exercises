#Solicitar al usuario que ingrese un numero 
numero=int(input("Ingrese num: "))

#Bucle para generar y mostrar las potencias de 2 desde 0 hasta numero ingresado
for i in range(numero + 1):
    print(2**i, end =" ")