"""
Leia um vetor de 40 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.
"""
from utils import gerar_vetor

vetor = gerar_vetor(40)
vetor_atualizado = []
for i in vetor:
	if i < 0:
		vetor_atualizado.append(0)
		continue
	vetor_atualizado.append(i)

print('Vetor original:', vetor)
print('Vetor atualizado:', vetor_atualizado)