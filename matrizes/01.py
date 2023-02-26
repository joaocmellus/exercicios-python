"""
Leia um vetor de 12 posições e em seguida ler também dois valores X e Y quaisquer correspondentes a duas posições no vetor.
Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.
"""
from utils import gerar_vetor

vetor = gerar_vetor(12)
pos_x = int(input('Insira o valor x: '))
pos_y = int(input('Insira o valor y: '))
resultado = vetor[pos_x] + vetor[pos_y]

print('Vetor:', vetor)
print('A soma dos valores nas posições X e Y:', resultado)