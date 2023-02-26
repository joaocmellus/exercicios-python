import random

def gerar_vetor(tamanho=1):
	return [random.randint(-10,50) for i in range(tamanho)]

def gerar_matriz(tamanho_x, tamanho_y):
	matriz = []
	for i in range(tamanho_y):
		matriz.append(gerar_vetor(tamanho_x))
	return matriz

def mostrar_matriz(matriz):
	for i, j in enumerate(matriz):
		print(i, j)