"""Altere o programa anterior para mostrar no final a soma dos números."""


a = int(input('Insira um número inteiro: '))
b = int(input('Insira outro número inteiro: '))

if a > b:
	a, b = b, a

soma = 0
for i in range(a, b+1):
	print(i)
	soma += i
print(f'A soma dos valores é: {soma}')