'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, 
informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário.
'''

# a = float(input('Insira o valor a: ')) 
# b = float(input('Insira o valor b: '))
# c = float(input('Insira o valor c: '))
a,b,c = 2, -6, 0
if a == 0:
    print('Essa não é uma equação do segundo grau!')
else:
    delta = (b**2) -4 * a * c  
    if delta < 0:
        print('A equação não possui raízes reais!')
    else:
        x1 = (-b + (delta**0.5))/ (2+a)
        if delta == 0:
            print(f'O resultado da equação é: {x1}')
        else:
            x2 = (-(b) - (delta**0.5))/ (2+a)
            print(f'Os resultados da equação são: {x1} e {x2}!')