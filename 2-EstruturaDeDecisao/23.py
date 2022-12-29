'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.'''

num = float(input('Insira um número: '))

if num//1 == num:
    print(f'{int(num)} é um número inteiro!')
else:
    print(f'{num} é um número decimal!')