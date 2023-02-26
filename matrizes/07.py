"""
Leia uma matriz 10 x 10 e escreva a localização (linha e a coluna) do maior valor.
"""
from utils import gerar_matriz, mostrar_matriz

matriz = gerar_matriz(10,10)

maior, valor_x, valor_y = None, None, None
for y, vetor in enumerate(matriz):
	for x, valor in enumerate(vetor):
		if not maior:
			maior = valor
			valor_y = y
			valor_x = x
		if valor > maior:
			maior = valor
			valor_y = y
			valor_x = x

mostrar_matriz(matriz)
print('O valor maior se encontra na posição:', valor_x, valor_y)