#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Insira um ano: '))
if ano % 4 == 0:
    mensagem = f'{ano} é um ano bissexto!'
else:
    mensagem = f'{ano} não é um ano bissexto!'

print(mensagem)