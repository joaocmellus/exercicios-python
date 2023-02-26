"""
Leia uma matriz 6 x 6, conte e escreva quantos valores maiores que 10 ela possui.
"""
from utils import gerar_matriz, mostrar_matriz

matriz = gerar_matriz(6,6)

valores = []
for vetor in matriz:
    for valor in vetor:
        if valor > 10:
            valores.append(valor)

mostrar_matriz(matriz)
print('A matriz possui', len(valores), 'valores maiores que 10')