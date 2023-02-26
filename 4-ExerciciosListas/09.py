# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
num = []

for i in range(10):
	num.append(int(input('Insira um número: ')))
quadrado = 0
for item in num:
	quadrado += item**2

print(num)
print('Soma dos quadrados:', quadrado)