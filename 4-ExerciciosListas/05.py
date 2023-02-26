# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

num = []
par = []
impar = []

for i in range(20):
	ins = int(input('Insira um número inteiro: '))
	num.append(ins)
	if ins%2 == 0:
		par.append(ins)
	else:
		impar.append(ins)

print('Números inseridos:', num)
print('Números pares:', par)
print('Números impares:', impar)