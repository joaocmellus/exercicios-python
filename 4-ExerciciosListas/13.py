# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
temperaturas = []

for i in meses:
	temperaturas.append(float(input('Insira a temperatura média do mês de {}: '.format(i))))

med = sum(temperaturas)/len(temperaturas)

print(f'Média anual de temperaturas: {med}ºC\n')
x = 0

print('Meses abaixo da média:')
for i in temperaturas:
	x += 1
	if i < med:
		print(f'{meses[x]}: {i}ºC')