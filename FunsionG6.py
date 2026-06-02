class FunsionG6:
    def __init__(self):
        pass

    # Estudiante 1: [Jean Pitti 8-1005-171]
        # Desarrollar una función que reciba una lista de números y retorne solo los números negativos.

    def numeros_negativos(self, lista: list) -> list:
        return [n for n in lista if n < 0]

    # Estudiante 2: [Yoseph Cortez 7-714-2261] 
        # Desarrollar una función que reciba una lista de números y retorne solo los números positivos.

    def filtrar_positivos(lista_numeros):
        lista_positivos = []
        
        
        for num in lista_numeros:
            if num > 0:
                lista_positivos.append(num)
                
        return lista_positivos

