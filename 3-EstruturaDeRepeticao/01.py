"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso 
o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

while True:
	num = input('Insira sua nota: ')
	try:
		float(num)
	except ValueError:
		print('Valor inválido')
		continue
	else:
		num = float(num)
		if num >= 0 and num <=10:
			print('Valor válido.')
			break
		else:
			print('Valor inválido.')
