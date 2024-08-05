def media(list_numeros):
    if len(list_numeros) == 0:
        return "La lista vacia"
    suma = sum(list_numeros)  
    cantidad = len(list_numeros)  
    media = suma / cantidad 
    return media


numeros = [10, 100, 1000]
resultado = media(numeros)
print("La media aritmética de la lista es", resultado)
