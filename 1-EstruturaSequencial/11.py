'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

a = int(input('Insira um número inteiro:\n'))

b = int(input('Insira um número inteiro:\n'))

c = float(input('Insira um número real:\n'))

calculo1 = (a*2) * (b/2)

calculo2 = (a*3) + c

calculo3 = c**3

print(f'Os resultados são:\n{calculo1}\n{calculo2}\n{calculo3}')