class FunsionG5:
    def __init__(self):
        pass

    # Estudiante 1: [Jean Pitti 8-1005-171]
        # Desarrollar una función que reciba una lista y retorne el valor máximo.
    def valor_maximo(self, lista: list) -> int:
        return max(lista) if lista else None

    # Estudiante 2: [Yoseph Cortez 7-714-2261] 
        # Desarrollar una función que reciba un número y calcule su factorial.

    def calcular_factorial(numero):
        if numero == 0 or numero == 1:
            return 1
        
        resultado = 1
        for i in range(2, numero + 1):
            resultado = resultado * i
            
        return resultado