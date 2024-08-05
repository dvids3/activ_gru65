def palindroma(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

palabra = input("Ingrese la palabra a ser analizada: ")
if palindroma(palabra):
    print('La palabra ingresada es palíndroma')
else:
    print('La palabra no es palíndroma')