# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range(10):
	numeros.append(int(input('Insira um número inteiro: ')))

numeros.reverse()

print(numeros)