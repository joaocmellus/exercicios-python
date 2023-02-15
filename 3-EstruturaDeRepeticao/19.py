"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""

conjunto = []

for i in range(10):
	while True:
		num = int(input('Insira um número inteiro entre 0 e 1000: '))
		if num >= 0 and num <= 1000:
			conjunto.append(num)
			break
		else:
			print('valor inválido\n')

maior = None
menor = None
for i in conjunto:
	if menor == None or i < menor:
		menor = i
	if maior == None or i > maior:
		maior = i
soma = sum(conjunto)

print(f'Maior número: {maior}\nMenor número: {menor}\nSoma dos Valores: {soma}')