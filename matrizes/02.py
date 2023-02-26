"""
Declare um vetor de 10 posições e o preencha com os 10 primeiros números impares e o escreva.
"""
vetor = []
contagem = 0
while len(vetor) != 10:
    if contagem % 2:
        vetor.append(contagem)
    contagem += 1

print(vetor)