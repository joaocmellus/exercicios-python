'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

a = int(input('Insira um número:\n'))
b = int(input('Insira um número:\n'))
c = int(input('Insira um número:\n'))
 
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

print(f'{maior} é o maior número e {menor} é o menor número!')
