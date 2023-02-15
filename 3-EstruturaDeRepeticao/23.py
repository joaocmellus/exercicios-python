"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""

def calcular_primos(max):
	divisoes = 0
	primos = []
	for num in range(2, maximo+1):
		e_primo = True
		for i in range(2, num):
			divisoes+=1
			if num%i == 0:
				e_primo = False
				break
				
		if e_primo:
			primos.append(num)			
	return primos, divisoes

def calcular_primos_otimizada(max):
	divisoes = 0
	primos = []
	for num in range(2, maximo+1):
		if not primos:
			primos.append(num)
		else:
			e_primo = True
			metade = len(primos)//2
			for i in primos[:metade]:
				divisoes+=1
				if num%i == 0:
					e_primo = False
					break
	
			if e_primo:
				primos.append(num)	
	return primos, divisoes

maximo = int(input('Insira um número inteiro: '))

print()
print('Calculo normal:')
primos, divisoes = calcular_primos(maximo)
print('Número primos:', primos)
print('Total de divisões realizadas', divisoes)

print()
print('Calculo otimizado:')
primos, divisoes = calcular_primos_otimizada(maximo)
print('Número primos:', primos)
print('Total de divisões realizadas', divisoes)