# Solicitar numero al usuario
numero=int(input("Ingrese numero: "))

#Resultado de todos los divisore de 'numero'
for i  in range(1, numero + 1):
    if numero % i == 0:
        print(i,end=" ")