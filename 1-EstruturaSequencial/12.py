'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
'''

altura = float(input('Qual a sua altura?\n'))

print('Seu peso ideal é {:.2f}Kg'.format((72.7*altura) - 58))