"""
Leia duas matrizes 4 x 4 e escreva uma terceira com os 4 maiores elementos entre as primeiras
"""
from utils import gerar_matriz, mostrar_matriz

matriz_a = gerar_matriz(4,4)
matriz_b = gerar_matriz(4,4)

matriz_c = [[], []]
for i in matriz_a:
    matriz_c[0].extend(i)

for i in matriz_b:
    matriz_c[1].extend(i)

for i in matriz_c:
    i.sort()

for i, vetor in enumerate(matriz_c):
    matriz_c[i] = vetor[-4:]

mostrar_matriz(matriz_a)
print()
mostrar_matriz(matriz_b)
print()
mostrar_matriz(matriz_c)