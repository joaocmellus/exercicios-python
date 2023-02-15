"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo."""

n = int(input('Insira um número inteiro: '))

print(f'A sequência Fibonacci até o {n}º número é:')

a = 0
b = 0
for i in range(n):
	novo = a + b
	if novo == 0:
		novo = 1
	a = b
	b = novo

print(novo)	