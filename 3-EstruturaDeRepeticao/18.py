"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

conjunto = []

for i in range(10):
	conjunto.append(int(input('Insira um número inteiro: ')))

maior = None
menor = None
for i in conjunto:
	if menor == None or i < menor:
		menor = i
	if maior == None or i > maior:
		maior = i
soma = sum(conjunto)

print(f'Maior número: {maior}\nMenor número: {menor}\nSoma dos Valores: {soma}')