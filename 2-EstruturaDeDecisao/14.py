'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0        A
Entre 7.5 e 9.0         B
Entre 6.0 e 7.5         C
Entre 4.0 e 6.0         D
Entre zero e 4.0        E
'''
a = float(input('Insira sua nota: '))
b = float(input('Insira sua nota: '))

med = (a+b)/2

if med > 0 and med < 4.0:
    conceito = 'E'
    mensagem = 'REPROVADO'
elif med < 6.0:
    conceito = 'D'
    mensagem = 'REPROVADO'
elif med < 7.5:
    conceito = 'C'
    mensagem = 'APROVADO'
elif med < 9.0:
    conceito = 'B'
    mensagem = 'APROVADO'
elif med < 10.0:
    conceito = 'A'
    mensagem = 'APROVADO'

print(f'Média: {med:.2f}\nConceito: {conceito}\nAluno(a) {mensagem}')