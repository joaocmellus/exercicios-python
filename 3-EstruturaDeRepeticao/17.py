"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""

n = int(input('Insira um número inteiro para ser fatorado: '))

valor = 1
for i in range(1, n+1):
	valor = valor * i

print(f'!{n} =', valor)