'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
print(''''Que turno você estuda?
    M - Matutino
    V - Vespertino
    N - Noturno
''')
t = input().lower()

if t == 'm':
    print('Bom Dia!')
elif t == 'v':
    print('Boa Tarde!')
elif t == 'n':
    print('Boa Noite!')
else:
    print('Opção inválida!')