'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

a1 = float(input('Insira sua primeira nota: '))
a2 = float(input('Insira sua segunda nota: '))
a3 = float(input('Insira sua terceira nota: '))
a4 = float(input('Insira sua quarta nota: '))

n = a1 + a2 + a3 + a4

med = n / 4

print('Sua média é de {:.2f}'.format(med))