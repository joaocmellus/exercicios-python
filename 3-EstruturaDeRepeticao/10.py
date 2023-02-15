"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."""

a = int(input('Insira um número inteiro: '))
b = int(input('Insira outro número inteiro: '))

if a > b:
	a, b = b, a

for i in range(a, b+1):
	print(i)