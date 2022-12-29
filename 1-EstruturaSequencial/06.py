'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

raio = float(input('Insira o raio:\n'))

if raio <= 0:
	print('Número inválido.')
else:
	area = 2 * 3.14 * raio**2
	print(f'Resultado da Área: {area}')