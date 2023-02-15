"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem."""

base = int(input('Insira um número base: '))
expoente = int(input('Insira um expoente: '))
resultado = base
for i in range(1, expoente):
	resultado = resultado * base
print(resultado)