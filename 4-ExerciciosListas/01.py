#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []

for i in range(5):
	numeros.append(int(input('Insira um número inteiro: ')))

print(numeros)