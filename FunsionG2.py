# Estudiante 2: [Yoseph Cortez 7-714-2261]

def calcular_promedio(lista_numeros):
    
    if len(lista_numeros) == 0:
        return 0
    
    suma_total = sum(lista_numeros)
    cantidad = len(lista_numeros)
    promedio = suma_total / cantidad
    
    return promedio

class FunsionG2:

    def __init__(self):
        pass

    # Estudiante 1:
        # Desarrollar una función que reciba una lista de números y calcule la suma total.

    def sumTotal(self, x):
        num = 0
        for j in x:
            num = num + j
        return "la suma de los numeros es: " + str(num)

    # Estudiante 2:
        # Desarrollar una función que reciba una lista de números y calcule el promedio.

    def calcular_promedio(lista_numeros):
        
        if len(lista_numeros) == 0:
            return 0
        
        suma_total = sum(lista_numeros)
        cantidad = len(lista_numeros)
        promedio = suma_total / cantidad
        
        return promedio