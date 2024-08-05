def nfactorial(n):
    if n < 0:
        return "sin numero negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

numero = int(input("escribe numero"))
resultado = nfactorial(numero)
print("El factorial de", numero, "es", resultado)