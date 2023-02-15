"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial 
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16."""

while True:
	n = int(input('Insira um número inteiro para ser fatorado: '))

	valor = 1
	for i in range(1, n+1):
		valor = valor * i

	print(f'!{n} =', valor)
	print()
	p = input('Deseja calcular novamente?(s/n)').lower()
	if p == 'n':
		break