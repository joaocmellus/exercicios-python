"""
Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida
"""
from utils import gerar_matriz, mostrar_matriz

matriz = gerar_matriz(5,5)

for i, vetor in enumerate(matriz):
	for j, valor in enumerate(vetor):
		if j == i:
			matriz[i][j] = 1
		else:
			matriz[i][j] = 0

mostrar_matriz(matriz)