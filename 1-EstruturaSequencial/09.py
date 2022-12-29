'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.'''

F = float(input('Insira a temperatura em ºF:\n'))

C = 5 * ((F-32) / 9)

print(f'{F}ºF equivale a {C:.3f}ºC')