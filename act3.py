import random

cantidad = int(input("ingresa numero"))
num_aleatorios = [random.randint(0, 100) 
for i in range(cantidad)]
print("Numeros aleatorios", num_aleatorios)

