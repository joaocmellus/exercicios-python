"""
Leia uma matriz 8 x 8 e a transforme numa matriz triangular inferior, atribuindo zero a todos os elementos acima da diagonal principal, escrevendo-a ao final.
"""
from utils import gerar_matriz, mostrar_matriz

matriz = gerar_matriz(8,8)

for y, vetor in enumerate(matriz):
	for x, valor in enumerate(vetor):
		if x <= y:
			matriz[y][x] = 1
		else:
			matriz[y][x] = 0

mostrar_matriz(matriz)