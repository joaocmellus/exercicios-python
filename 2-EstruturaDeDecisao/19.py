'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

num = list(input('Insira um Número: ').strip())

if len(num) == 3:
    centena = num[0]
    if centena == '1':
        print(centena, 'centena', end=', ')
    else:
        print(centena, 'centenas', end=', ')
if len(num) >= 2:
    dezena = num[-2]
    if dezena == '1':
        print(dezena, 'dezena', end=' e ')
    else:
        print(dezena, 'dezenas', end=' e ')
if len(num) >= 1:
    unidade = num[-1]
    if unidade == '1':
        print(unidade, 'unidade')
    else:
        print(unidade, 'unidade')
