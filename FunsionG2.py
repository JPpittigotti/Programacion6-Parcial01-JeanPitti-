















# Estudiante 2: [Yoseph Cortez 7-714-2261]

def calcular_promedio(lista_numeros):
    
    if len(lista_numeros) == 0:
        return 0
    
    suma_total = sum(lista_numeros)
    cantidad = len(lista_numeros)
    promedio = suma_total / cantidad
    
    return promedio
