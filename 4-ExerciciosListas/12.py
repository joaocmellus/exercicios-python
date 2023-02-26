# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

pessoas = []
med = []
inf = 0

for i in range(30):
	print(f'{i+1}ª pessoa')
	idade = int(input('Insira a idade da pessoa: '))
	altura = float(input('Insira a altura da pessoa: '))
	pessoas.append([idade, altura])
	med.append(altura)
	print()

med = sum(med)/len(med)

for i in pessoas:
	if i[0] > 13 and i[1] < med:
		inf += 1

print(f'{inf} alunos tem altura menor que a média')