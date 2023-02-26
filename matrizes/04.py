"""
Leia um vetor de 20 posições e em seguida um valor X qualquer. Seu programa devera fazer 
uma busca do valor de X no vetor lido e informar a posição em que foi encontrado ou se não foi encontrado.
"""
from utils import gerar_vetor

vetor = gerar_vetor(20)
print('vetor:',vetor)
valor = int(input('Insira um valor: '))
if valor in vetor:
	print('O valor informado está na posição:', vetor.index(valor))
else:
	print('O valor informado não foi encontrado.')