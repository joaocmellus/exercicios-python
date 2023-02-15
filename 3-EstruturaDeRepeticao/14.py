"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."""
numeros = []
for i in range(10):
	numeros.append(int(input('Insira um número inteiro: ')))
par = 0
impar = 0
for i in numeros:
	if i%2 == 0:
		par += 1
	else:
		impar += 1
print(f'Você digitou: {par} números pares e {impar} números ímpares!')
