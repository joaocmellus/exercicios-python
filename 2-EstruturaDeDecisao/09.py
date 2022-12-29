'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

a = int(input('Insira um número: '))
b = int(input('Insira um número: '))
c = int(input('Insira um número: '))

if a > b and a > c:
    maior = a
    if b > c:
        meio, menor = b, c
    else:
        meio, menor = c, b

elif b > a and b > c:
    maior = b
    if a > c:
        meio, menor = a, c
    else:
        meio, menor = c, a

else:
    maior = c
    if b > a:
        meio, menor = b, a
    else:
        meio, menor = a, b


print(f'{maior} - é o maior número\n{meio} - é o segundo maior\n{menor} - é o menor número')