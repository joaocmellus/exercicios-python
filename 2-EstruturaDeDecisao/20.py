'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

a = float(input('Insira sua primeira nota: '))
b = float(input('Insira sua segunda nota: '))
c = float(input('Insira sua terceira nota: '))

med = (a+b+c)/3

if med >= 7 and med < 10:
    print('APROVADO')
elif med > 0  and med < 7:
    print('REPROVADO')
else:
    print('APROVADO COM DISTINÇÃO')