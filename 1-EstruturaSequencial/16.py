'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

metros = int(input('Qual o tamanho da área a ser pintada?\n'))
litros = metros/3

preçoL = 80
capacidadeL = 18

latas = litros//capacidadeL
if type(latas) is float:		#esse código eu que fiz u.u
	latas = latas + 1

total = latas*preçoL

print(f'''
Você usará {int(latas)} latas de tinta
O preço total é de: R${total:.2f}
''')