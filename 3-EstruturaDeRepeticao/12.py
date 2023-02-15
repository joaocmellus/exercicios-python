"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:"""

valor = int(input('Insira um número: '))

print(f'Tabuada do {valor}')
for multiplicador in range(1, 11):
	print(f'{valor} x {multiplicador} = {valor*multiplicador}')