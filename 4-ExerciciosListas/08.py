# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

pessoas = {}

for i in range(2):
	print(f'{i+1}ª pessoa')
	idade = int(input('Insira a idade da pessoa: '))
	altura = float(input('Insira a altura da pessoa: '))
	pessoas[i] = [idade, altura]
	print()

for i in pessoas:
	print(f'{i}ª pessoa: Altura:',pessoas[i][1], 'Idade:', pessoas[1][0])