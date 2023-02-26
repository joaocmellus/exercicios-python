"""
Leia um vetor de 40 posições. Contar e escrever quantos valores pares ele possui.
"""
from utils import gerar_vetor

vetor = gerar_vetor(40)
valores = []
for i in vetor:
	if not i % 2:
		valores.append(i)

print('Vetor:', vetor)
print('O vetor possui', len(valores),'valores pares:', valores)