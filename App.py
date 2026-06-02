from FunsionG1 import *
from FunsionG2 import *
from FunsionG3 import *
from FunsionG4 import *
from FunsionG5 import *
from FunsionG6 import *
from FunsionG7 import *

# Funsion1
G1 = FunsionG1()

print(G1.parOrImpar(6))
print(G1.parOrImpar(5))

#  Funsion2
G2 = FunsionG2()

x = [5,1,10]

print(G2.sumTotal(x))

# Funsion 3
G3 = FunsionG3()

palabra = "Patata"

print(G3.contar_caracteres(palabra))

# Funsion 4

G4 = FunsionG4()

numeros = [10, 20, 30, 40]
print(G4.contar_elementos(numeros))

# Funsion 5

G5 = FunsionG5()
numeros = [10, 20, 30, 40]

print(G5.valor_maximo(numeros))

# Funsion 6

G6 = FunsionG6()
lista = [-5, 0, 3, -2, 8]

print(G6.numeros_negativos(lista))


# Funsion 7

G7 = FunsionG7()

print(G7.convertir_mayusculas("hola mundo"))