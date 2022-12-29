'''Faça um Programa que leia três números e mostre o maior deles.'''

a = int(input('Insira um número:\n'))
b = int(input('Insira um número:\n'))
c = int(input('Insira um número:\n'))

if a > b and a > c:
    print(f'{a} é o maior número!')
elif b > a and b > c:
    print(f'{b} é o maior número!')
elif c > a and c > b:
    print(f'{c} é o maior número!')