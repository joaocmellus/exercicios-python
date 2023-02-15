"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500."""

a = 0
b = 0
novo = a + b
n = 0
while 500 > novo:
	novo = a + b
	if novo == 0:
		novo = 1
	a = b
	b = novo
	n += 1
	print(novo)

print(f'O valor de Fibonacci é maior que 500 a partir da {n}ª série.')