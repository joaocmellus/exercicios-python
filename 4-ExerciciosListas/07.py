# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

num = []

for i in range(5):
	num.append(int(input('Insira um número inteiro: ')))
mult = 1
for i in num:
	mult *= i 

print(f'Soma: {sum(num)}')
print(f'Multiplicação: {mult}')
print(f'Números:', num)