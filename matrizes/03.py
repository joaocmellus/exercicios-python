"""
Leia um vetor de 16 posições e troque os 8 primeiros valores pelos 8 últimos e vice-e-versa. Escreva ao final o vetor obtido.')
"""
from utils import gerar_vetor

vetor = gerar_vetor(16)
vetor_atualizado = vetor[8:] + vetor[:8]

print('vetor original:', vetor)
print('vetor atualizado:', vetor_atualizado)