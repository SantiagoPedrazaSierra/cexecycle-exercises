#Solicitar tiempo total en 0
tiempo_total= 0

#Bucle para pedir a usuario tiempo de cada tramo
while True:
    duracion=int(input("Duracion tramo: "))
    if duracion == 0:
        break #Finaliza cuando se ingrese 0
    tiempo_total += duracion #Suma la duracion del tramo al tiempo total

#Operacion para convertir tiempo total a horas y minutos
horas = tiempo_total // 60
minutos = tiempo_total % 60

#Resultado de tiempo en horas:minutos
print(f"Tiempo total de viaje: {horas}:{minutos:02} horas")