'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

a = float(input('Insira o valor do primeiro produto: '))
b = float(input('Insira o valor do segundo produto: '))
c = float(input('Insira o valor do terceiro produto: '))

if a < b and a < c:
    print('\nVocê deve comprar o primeiro produto')
elif b < a and b < c:
    print('\nVocê deve comprar o segundo produto')
elif c < a and c < b:
    print('\nVocê deve comprar o terceiro produto')

