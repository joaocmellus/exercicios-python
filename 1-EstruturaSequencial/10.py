'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

C = float(input('Insira a temperatura em ºC:\n'))

F = 32 + ((C/5) * 9)

print(f'{C}ºF equivale a {F:.3f}ºC')