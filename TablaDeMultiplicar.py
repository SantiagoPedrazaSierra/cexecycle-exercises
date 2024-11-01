#Pedir ingreso del tamaño  de la tabla 
tamaño=10

#tabla de multiplicar
for i in range(1,tamaño + 1):
    for j in range(1, tamaño + 1):
        
#Calculo de el producto y mostrarlo al usuario
        print(""f"{i * j:4}", end="")
    print() #Salto de linea terminando cada fila 
    