'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

l1 = float(input('Insira o tamanho do primeiro lado do triângulo: '))
l2 = float(input('Insira o tamanho do segundo lado do triângulo: '))
l3 = float(input('Insira o tamanho do terceiro lado do triângulo: '))

if not 0 in (l1, l2, l3):
    if l1 <= l2 + l3 and l2 <= l1 + l3 and l3 <= l1 + l2:
        triângulo = True
    else:
        triângulo = False
        print('Esse triângulo não existe!')

    if triângulo == True:
        if l1 == l2 == l3:
            print('Esse é um triângulo equilátero!')
        elif l1 != l2 and l1 != l3 and l2 != l3:
            print('Esse é um triângulo escaleno!')
        else:
            print('Esse é um triângulo isósceles!')
else:
    print('Esse triângulo não existe!')