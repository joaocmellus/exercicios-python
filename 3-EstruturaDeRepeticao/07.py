"""Faça um programa que leia 5 números e informe o maior número."""

lista = []
for i in range(5):
	lista.append(int(input('Insira um número: ')))

maior = None
for i in lista:
	if maior == None:
		maior = i
	if i > maior:
		maior = i

print(f'O número maior é: {maior}')