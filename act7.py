numeros = [10, 100, 1000, 10000, 100000, 1000000]

num_mas_grande = numeros[0]
num_mas_pequeno = numeros[0]

for numero in numeros:
    if numero > num_mas_grande:
        num_mas_grande = numero
    if numero < num_mas_pequeno:
        num_mas_pequeno = numero

print("El numero mas grande es", num_mas_grande)
print("El numero mas pequeño es", num_mas_pequeno)