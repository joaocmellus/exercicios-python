'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

operacao = int(input('Qual operação deseja realizar?\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão'))
a = float(input('Insira um número: '))
b = float(input('Insira um número: '))
if operacao in (1,2,3,4):
    if operacao == '1':
        res = a+b
    elif operacao == '2':
        res = a-b
    elif operacao == '3':
        res = a*b
    else:
        res = a/b
    
    if res%2 == 0:
        c = 'par'
    else:
        c = 'impar'
    
    if res < 0:
        d = 'negativo'
    else:
        d = 'positivo'
    
    if res//1 == res:
        e = 'inteiro'
        res= int(res)
    else: 
        e = 'decimal'
    
    print(f'O resultado é: {res}')
    print(f'{res} é um número {c}, {d} e {e}.')
else:
    print('Opção Inválida! Tente outro número!')