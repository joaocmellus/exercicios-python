"""
Leia uma matriz 20 x 20. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, 
ao final escrever a localização (linha e coluna) ou uma mensagem de “não encontrado”.
"""
from utils import gerar_matriz, mostrar_matriz

matriz = gerar_matriz(20,20)

mostrar_matriz(matriz)
v = int(input('Insira o valor para a busca: '))

coordenadas = []
for y, vetor in enumerate(matriz):
	for x, valor in enumerate(vetor):
		if valor == v:
			coordenadas.append((x, y))

if not coordenadas:
	print('O valor', v, 'não se encontra na matriz')
else:
	print('O valor', v, 'se encontra nas posições:', coordenadas)