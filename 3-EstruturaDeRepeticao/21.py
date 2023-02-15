"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

num = int(input('Insira um número inteiro: '))

e_primo = True

for i in range(2, num):
	if not num%i:
		e_primo = False
		break

if e_primo:
	print(f'{num} é um número primo')
else:
	print(f'{num} não é um número primo')