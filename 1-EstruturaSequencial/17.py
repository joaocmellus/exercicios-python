'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

metros = int(input('Qual o tamanho da área a ser pintada?\n'))
litros = metros/6

preço_galão = 25
preço_lata = 80

capacidade_galão = 3.6
capacidade_lata = 18

latas = litros/capacidade_lata
if type(latas) is float:
	latas+= 1
	latas = int(latas)

preço1 = latas*80.00

galões = litros/capacidade_galão
if type(galões) is float:
	galões+= 1
	galões = int(galões)
preço2 = galões*25.00

restos = litros//capacidade_lata
restos = int(restos)
galões2 = (litros - restos)/capacidade_galão
if galões2 < 0:
	galões2 = 0
if type(galões2) is float:
	galões2+= 0 
	galões2 = int(galões2)

preço3 = (restos*80.00) + (galões2*25.00)


print(f'Você usará {latas} latas de 18 litros, custará R${preço1:.2f}')
print(f'Você usará {galões} galões de 3,6 litros, custará R${preço2:.2f}')
print(f'Você usará {restos} latas e {galões2} galões, custará R${preço3:.2f}')