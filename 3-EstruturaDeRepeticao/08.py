"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

lista = []
for i in range(5):
	lista.append(int(input('Insira um número: ')))
soma = sum(lista)
media = soma/len(lista)

print(f'A soma desses números é {soma}, e a média {media}')