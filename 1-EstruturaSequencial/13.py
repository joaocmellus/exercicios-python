'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

while True:
	gênero = input('Qual seu gênero?\n1.Masculino\n2.Feminino\n')
	if gênero == '1':
		break
	elif gênero == '2':
		break
	else:
		print('Opção inválida. Tente novamente.\n')
		continue

h = float(input('\nQual a sua altura?\n'))

if gênero == '1':
	calculo = (72.7*h) - 58
else:
	calculo = (62.1*h) - 44.7

print(f'\nO seu peso ideal é de {calculo:.2f}Kg')
