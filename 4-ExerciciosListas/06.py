# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# Eu fiz com dicionário porque entendi errado... :(

notas = {}

for i in range(10):
	nome = input('Insira o nome do aluno: ')
	if nome in notas.keys():
		continue
	nota = []
	for i in range(4):
		nota.append(int(input('Insira a nota do aluno: ')))
	med = sum(nota)/len(nota)
	notas[nome] = med
	print()

print('Alunos aprovados:')
for item in notas:
	if notas[item] >= 7:
		print(f'Aluno: {item}\nMédia: {notas[item]}\n')
