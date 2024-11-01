#Pedir a usuario ingrese numeros 
numero1= int(input("Ingrese num: "))
numero2= int(input("Ingrese num: "))

#Asegurar que numero es mayor y que menor 
inicio= min(numero1,numero2) + 1
fin= max(numero1, numero2)

#Operacion de la suma de los numeros entre numero1 y numero2
suma= sum(range(inicio,fin))

#Mostrar resultado
print("la suma es ",suma)
