'''Faça um Programa que converta metros para centímetros.'''

m = float(input('Insira uma medida em metros:\n'))

cm = int(m * 100)

if m == 1:
	print(f'{m} metro = {cm} centímetros')
else:
	print(f'{m} metros = {cm} centímetros')