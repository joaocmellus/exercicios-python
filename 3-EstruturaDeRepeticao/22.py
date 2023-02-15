"""Altere o programa de cálculo dos números primos, informando, 
caso o número não seja primo, por quais número ele é divisível."""

num = int(input('Insira um número inteiro: '))

e_primo = True
divisiveis = []
for i in range(1, num+1):
	if not num%i:
		if i not in (1, num):
			e_primo = False
		divisiveis.append(i)

if e_primo:
	print(f'{num} é um número primo')
else:
	print(f'{num} não é um número primo')
print(f'ele é divisível por:', divisiveis)