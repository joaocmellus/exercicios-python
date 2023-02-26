# Faça um Programa que leia 4 notas, mostre as notas e a média na tela
notas = []
for i in range(4):
	notas.append(float(input('Insira uma nota: ')))

print('notas:',notas)
print('soma das notas:', sum(notas))