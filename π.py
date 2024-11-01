#Solicitar al usuario que ingrese el numero 
n= int(input("n: "))

#Inicializa la variable para almacenar aprox de π
pi_aproximado = 0

#Bucle para calcular suma hasta el numero n 
for i in range(n):
    #Alternar el signo de cada termino y calcula el valor 
    pi_aproximado += (-1)** i * 4 / (2 * i + 1)

#Resultado de aprox π
print(pi_aproximado)